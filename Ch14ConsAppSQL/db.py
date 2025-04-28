import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv
import os

dotenv_path=os.path.join(os.path.dirname(__file__),".env")
load_dotenv(dotenv_path)

DB_PARAMS = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

connection_pool=pool.SimpleConnectionPool(1,10, **DB_PARAMS)
def get_connection():
    return connection_pool.getconn()
def release_connection(conn):
    connection_pool.putconn(conn)