from db import get_connection,release_connection

def create_table():
    conn=get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    department VARCHAR(100) NOT NULL,
                    salary NUMERIC(10,2) NOT NULL CHECK (salary > 0)
                );
            """)
            conn.commit()
            print("'employees' table created successfully(if not exists)");
    except Exception as e:
        print("Error while creating table",e)
        conn.rollback()
    finally:
        release_connection(conn)
if __name__ == "__main__":
    create_table()