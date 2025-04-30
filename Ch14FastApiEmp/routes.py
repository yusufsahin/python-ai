from fastapi import APIRouter
from crud import add_employee
from models import EmployeeCreate

router = APIRouter()

@router.post("/employee", response_model=int)
async def add_employee_route(employee: EmployeeCreate):
    return await add_employee(employee)