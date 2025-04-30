from db import get_connection, release_connection

def add_employee(name,department,salary):
    conn= get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO employees (name,department,salary) VALUES (%s,%s,%s)",
                        (name,department,salary)
                        )
            conn.commit()
            print("Employee added successfully")
    except Exception as e:
        print("Error : ",e)
        conn.rollback()
    finally:
        release_connection(conn)
def list_employees():
    with  get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id,name,department,salary FROM employees")
            rows = cur.fetchall()
            for row in rows:
                print(row)

def update_employee(p_emp_id,p_name, p_department, p_salary):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE employees SET name=%s,department=%s,salary=%s WHERE id=%s",
                (p_name,p_department,p_salary,p_emp_id)
            )
            conn.commit()

def delete_employee(emp_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM employees WHERE id=%s",(emp_id,))
            conn.commit()
def get_employee_by_id(emp_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, department, salary FROM employees WHERE id=%s",
                (emp_id,)
            )
            row = cur.fetchone()
            return row
