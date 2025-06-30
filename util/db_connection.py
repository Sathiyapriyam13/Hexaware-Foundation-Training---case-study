import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Poojashree",   # ✅ change to your actual password
        database="cars"
    )
