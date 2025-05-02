from fastapi import APIRouter
from crud import add_employee, list_employees
from models import EmployeeCreate, EmployeeOut
from typing import List
router = APIRouter()

@router.post("/employee", response_model=int)
async def add_employee_route(employee: EmployeeCreate):
    return await add_employee(employee)

@router.get("/employee", response_model=List[EmployeeOut])
async def get_employee_route():
    return  await list_employees()