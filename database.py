import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ak@200730278",
            database="bloodlink_db",
            port=3306
        )
        if connection.is_connected():
            return connection

    except Error as error:
        print("MySQL connection failed:", error)

    return None