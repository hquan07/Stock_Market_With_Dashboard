import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Huyquan160720040@",
            database="stocksdb"
        )
        if conn.is_connected():
            print("✅ MySQL connection successful!")
            return conn
    except Error as e:
        print("❌ MySQL connection error:", e)
        return None