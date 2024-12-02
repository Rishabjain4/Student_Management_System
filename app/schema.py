from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    city: str
    country: str

# Schema for creating a student
class StudentCreate(BaseModel):
    name: str
    age: int
    address: Address

class StudentDetail(BaseModel):
    name: str
    age: int

# Schema for responding with a student
class StudentResponse(BaseModel):
    id: str

class UpdateAddress(BaseModel):
    city: Optional[str]=None
    country: Optional[str]=None

# Schema for updating a student
class StudentUpdate(BaseModel):
    name: Optional[str]=None
    age: Optional[int]=None
    address: Optional[UpdateAddress]=None
    
class AllStudents(BaseModel):
    data: Optional[list[StudentDetail]]=None
    