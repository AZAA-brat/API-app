# Cars API

A small REST API for managing cars, built with FastAPI and SQLite.

## Requirements

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

Install:

```
pip install fastapi pydantic uvicorn
```

## Run

From the project folder:

```
uvicorn main:app --reload
```

Then open:

- API docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/api/ping

The database file `cars.db` is created automatically on first start.

## Endpoints

| Method | Path | Description | Success status |
|---|---|---|---|
| GET | `/api/ping` | Health check | 200 |
| GET | `/api/cars` | List all cars | 200 |
| GET | `/api/cars/{car_id}` | Get one car | 200 |
| POST | `/api/cars` | Add a car | 201 |
| PUT | `/api/cars/{car_id}` | Update a car (send only the fields to change) | 200 |
| DELETE | `/api/cars/{car_id}` | Delete a car | 204 |

Unknown `car_id` returns 404.

## Data

Each car has:

| Field | Type | Set by | Notes |
|---|---|---|---|
| `id` | integer | server | Assigned automatically |
| `name` | string | client | 1–100 characters |
| `price` | number | client | Must be greater than 0 |
| `created_at` | datetime | server | UTC, ISO 8601 |

## Example

Create a car:

```
POST /api/cars
{"name": "Chevrolet Malibu", "price": 25000}
```

Update only the price:

```
PUT /api/cars/1
{"price": 23000}
```