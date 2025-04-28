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