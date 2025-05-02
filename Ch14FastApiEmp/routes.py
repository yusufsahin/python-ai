from http.client import HTTPException

from fastapi import APIRouter
from crud import add_employee, list_employees, update_employee, delete_employee, get_employee_by_id
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

@router.get("/employee/{emp_id}", response_model=EmployeeOut)
async def get_employee_route(emp_id: int):
    employee= await  get_employee_by_id(emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee