"""
Library management module
"""
from app.extensions import Database
import mysql.connector
from mysql.connector import errorcode

class LibraryManager:

    def __init__(self, library_info):
        self.library_info = library_info

    
    def add_library(self):
        conn = Database.db_connection()

        cursor = conn.cursor()
        query = "INSERT INTO Libraries (name, description, logo_url) VALUES (%s, %s, %s)"

        try:
            cursor.execute(query, (self.library_info[0], self.library_info[1], self.library_info[2]))

        except mysql.connector.Error as e:
            return {"success": False, "message": f"Exception: {e}"}
        
        else:
            conn.commit()
            if cursor.rowcount > 0:
                return {"success": True, "message": f"Welcome to ShelfSync {self.library_info[0]}"}
            return {"success": False, "message": f"Could not save the library. Error: {cursor.fetchwarnings}"}
        
        finally:
            Database.db_clean_up(conn, cursor) 

    def delete_library(self):
        conn = Database.db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM Libraries WHERE name = %s AND description = %s"

        try:
            cursor.execute(query, (self.library_info[0], self.library_info[1]))

        except mysql.connector.Error as e:
            return {"success": False, "message": f"Exception: {e}"}
        
        else:

            if cursor.rowcount > 0:
                return {"success": True, "message": f"{self.library_info[0]} has been succesfully deleted"}
            return {"success": False, "message": f"Could not delete library. Error: {cursor.fetchwarnings}"}
        
        finally:
            Database.db_clean_up(conn, cursor)

    def edit_library(self):
        pass

    def search_by_name(self):
        pass

    def search_by_location(self):
        pass