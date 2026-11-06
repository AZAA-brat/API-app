from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from utils.database import get_db, init_db
from app.classes import Car, CarIn, CarUpdate
from functions.row import row_to_car

app = FastAPI(
    title="Cars App",
    version = "1.0.0"
)

init_db()


@app.get("/api/ping")
def ping():
    return {"status": "ok"}


@app.get("/api/cars", response_model=list[Car])
def list_cars():
    with get_db() as db:
        rows = db.execute("SELECT * FROM cars ORDER BY car_id").fetchall()
    return [row_to_car(row) for row in rows]


@app.get("/api/cars/{car_id}", response_model=Car)
def get_car(car_id: int):
    with get_db() as db:
        row = db.execute("SELECT * FROM cars WHERE car_id = ?", (car_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return row_to_car(row)


@app.post("/api/cars", response_model=Car, status_code=201)
def create_car(car: CarIn):
    created_at = datetime.now(timezone.utc).isoformat()
    with get_db() as db:
        cursor = db.execute(
            "INSERT INTO cars (name, price, created_at) VALUES (?, ?, ?)",
            (car.name, car.price, created_at),
        )
        car_id = cursor.lastrowid
    return Car(id=car_id, name=car.name, price=car.price, created_at=created_at)


@app.put("/api/cars/{car_id}", response_model=Car)
def update_car(car_id: int, car: CarUpdate):
    with get_db() as db:
        existing = db.execute("SELECT * FROM cars WHERE car_id = ?", (car_id,)).fetchone()
        if existing is None:
            raise HTTPException(status_code=404, detail="Car not found")

        new_name = car.name if car.name is not None else existing["name"]
        new_price = car.price if car.price is not None else existing["price"]

        db.execute(
            "UPDATE cars SET name = ?, price = ? WHERE car_id = ?",
            (new_name, new_price, car_id),
        )
    return Car(
        id=car_id,
        name=new_name,
        price=new_price,
        created_at=existing["created_at"],
    )


@app.delete("/api/cars/{car_id}", status_code=204)
def delete_car(car_id: int):
    with get_db() as db:
        cursor = db.execute("DELETE FROM cars WHERE car_id = ?", (car_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Car not found")








