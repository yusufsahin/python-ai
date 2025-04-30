from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    department: str
    salary: float

class EmployeeUpdate(EmployeeCreate):
    pass

class EmployeeOut(EmployeeCreate):
    id: int