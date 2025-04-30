from database import get_connection
from models import  EmployeeCreate

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