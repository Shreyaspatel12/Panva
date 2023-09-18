# database.py

import mysql.connector
from app.config import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as error:
        raise Exception(f"Unable to connect to the database. Error: {str(error)}")
