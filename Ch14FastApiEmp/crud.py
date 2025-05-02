from database import get_connection
from models import  EmployeeCreate
from typing import  List,Dict

async def create_table():
    conn = await get_connection()
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            department VARCHAR(100),
            salary NUMERIC
        )
    """)
    await conn.close()

async  def add_employee(data: EmployeeCreate)->int:
    conn = await get_connection()
    row = await conn.fetchrow("""
        INSERT INTO employees (name, department, salary)
        VALUES ($1, $2,$3 )
        RETURNING id
    """, data.name, data.department, data.salary)
    await conn.close()
    return row["id"]

async def list_employees() -> List[Dict]:
    conn = await get_connection()
    try:
        rows = await conn.fetch("SELECT id, name, department, salary FROM employees ORDER BY id")
        return [
            {"id": row["id"], "name": row["name"], "department": row["department"], "salary": float(row["salary"])}
            for row in rows
        ]
    finally:
        await conn.close()
