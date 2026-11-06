from pydantic import BaseModel, Field
from datetime import datetime

class CarIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)

class CarUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    price: float | None = Field(default=None, gt=0)

class Car(BaseModel):
    id: int
    name: str
    price: float
    created_at: datetime

