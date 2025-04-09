import sqlite3

def create_connection():
    return sqlite3.connect("mydb.sqlite3")

def create_table(conn):
    with conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                salary REAL
            )
        ''')

def insert_employee(conn, name, salary):
    with conn:
        conn.execute('''
            INSERT INTO employees (name, salary) VALUES (?, ?)
        ''', (name, salary))

def fetch_employees(conn):
    with conn:
        cursor = conn.execute('SELECT * FROM employees')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def main():
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT sqlite_version();")
        db_version = cursor.fetchone()
        print(f"Database version: {db_version[0]}")

        create_table(conn)

        insert_employee(conn, 'John Doe', 50000)
        insert_employee(conn, 'Jane Doe', 100000)

        fetch_employees(conn)

    finally:
        conn.close()

if __name__ == '__main__':
    main()
