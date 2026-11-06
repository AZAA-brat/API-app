from app.classes import Car
def row_to_car(row) -> Car:
    return Car(
        id=row["id"],
        name=row["name"],
        price=row["price"],
        created_at=row["created_at"]
    )