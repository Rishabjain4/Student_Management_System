from pydantic import BaseModel, Field
from typing import Optional

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

    class Config:
        allow_population_by_field_name = True
