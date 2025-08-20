"""
Library management module
"""
from app.extensions import Database
import mysql.connector
from mysql.connector import errorcode

class LibraryManager:

    @staticmethod
    def add_library(library):
        conn = Database.db_connection()

        cursor = conn.cursor()
        query = "INSERT INTO Libraries (name, description, logo_url) VALUES (%s, %s, %s)"

        try:
            cursor.execute(query, (library.name, library.description, library.logo_url))

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                return {"success": False, "message": "Error. library already exists."}
            return {"success": False, "message": "Oops! We ran into a problem."}
        
        else:
            conn.commit()
            if cursor.rowcount > 0:
                return {"success": True, "message": f"Welcome to ShelfSync {library.name}"}
            return {"success": False, "message": f"Could not save the library. Error: {cursor.fetchwarnings()}"}
        
        finally:
            Database.db_clean_up(conn, cursor) 

    @staticmethod
    def delete_library(library):
        conn = Database.db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM Libraries WHERE name = %s AND description = %s"

        try:
            cursor.execute(query, (library.name, library.description))

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ROW_IS_REFERENCED_2:
                return {"sucess": False, 
                        "message": "Error: Library could not be deleted. Clear library data first."}
            return {"success": False, "message": "Oops! We ran into a problem."}
        
        else:
            conn.commit()
            if cursor.rowcount > 0:
                return {"success": True, "message": f"{library.name} has been succesfully deleted"}
            return {"success": False, "message": "Could not delete library. Delete all users and transactions and try again."}
        
        finally:
            Database.db_clean_up(conn, cursor)



    @staticmethod
    def get_libraries():
        conn = Database.db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Libraries"

        try:
            cursor.execute(query)
            results = cursor.fetchall()

        except mysql.connector.Error as err:
            return {"success": False, "message": "Oops! We ran into a problem. Please try again."}
        
        else:
            if cursor.rowcount > 0:
                return {"success": True, "message": "Operation successful", "data": results}
            return {"success": False, "message": "No libraries."}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def search_by_name(name):
        conn = Database.db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Libraries WHERE name LIKE %s"

        try:
            cursor.execute(query, (f"%{name}%",))
            results = cursor.fetchall()

        except mysql.connector.Error as err:
            return {"success": False, "message": "Oops! We ran into a problem. Try again later."}
        
        else:
            if cursor.rowcount > 0:
                return {"success": True, "message": "Operation successful", "data": results}
            return {"success": True, "message": "No Match. Check the library name and try again.", "data": []}
        
        finally:
            Database.db_clean_up(conn, cursor)


    @staticmethod
    def edit_library(new_library_info, library_id):
        conn = Database.db_connection()
        cursor = conn.cursor()
        query = "UPDATE Libraries SET name = %s, description = %s, logo_url = %s WHERE id = %s"

        try:
            cursor.execute(query, (new_library_info.name, 
                                   new_library_info.description, 
                                   new_library_info.logo_url, 
                                   library_id))
            
        except mysql.connector.Error as err:
            return {"success": False, "message": f"{err}"}
        
        else:
            conn.commit()
            if cursor.rowcount > 0:
                return {"success": True, "message": "Library updated successfully"}
            return {"success": False, "message": "Oops! We ran into a problem. Try again later."}
        
        finally:
            Database.db_clean_up(conn, cursor)