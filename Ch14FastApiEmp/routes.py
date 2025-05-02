from fastapi import APIRouter
from crud import add_employee, list_employees, update_employee, delete_employee
from models import EmployeeCreate, EmployeeOut, EmployeeUpdate
from typing import List
router = APIRouter()

@router.post("/employee", response_model=int)
async def add_employee_route(employee: EmployeeCreate):
    return await add_employee(employee)

@router.get("/employee", response_model=List[EmployeeOut])
async def get_employee_route():
    return  await list_employees()

@router.put("/employee/{emp_id}")
async def update_employee_route(emp_id: int, data: EmployeeUpdate):
    await update_employee(emp_id, data)
    return {"status": "updated"}

@router.delete("/employee/{emp_id}")
async def delete_employee_route(emp_id: int):
    await delete_employee(emp_id)
    return {"status": "deleted"}