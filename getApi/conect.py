
import psycopg2
try:
    credenciales = {
        "dbname": "emember",
        "user": "root",
        "password": "root",
        "host": "127.0.0.1",
        "port": 5432
    }
    conexion = psycopg2.connect(**credenciales)
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)