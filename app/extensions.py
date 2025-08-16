"""
DB connection and other tools for external integration
"""
import os
import mysql.connector
from app.config import db_host, db_user, db_password, db_name, db_port


class Database:

    @staticmethod
    def db_connection():
        conn = mysql.connector.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_name,
            port = db_port
        )

        if conn:
            print("Connected to Database!")
            return conn
        else:
            print("Could not connect to the Database.")
            return []
        
    @staticmethod
    def db_clean_up(connection, cursor):
        cursor.close()
        connection.close()
        
    @staticmethod
    def create_db(connection):

        cursor = connection.cursor()

        try:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            sql_file = os.path.join(BASE_DIR, "database.sql")

            with open(sql_file, "r") as f:
                cursor.execute(f.read(), multi=True)

        except mysql.connector.Error as e:

            return f"Error: {e}"
        
        else:

            if cursor.warning_count < 1:
                return "Database Susscessfully created!"
            return "Error creating DB"
        
        finally:
            cursor.close()
            connection.close()


