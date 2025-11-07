"""
Library management module
"""
from app.extensions import Database
import mysql.connector
from mysql.connector import errorcode

class LibraryManager:

    @staticmethod
    def add_library(library):
        """
        Add a new library to the Database
        """

        conn = Database.db_connection()

        cursor = conn.cursor()
        query = "INSERT INTO Libraries (name, description, logo_url, coordinates) VALUES (%s, %s, %s, %s)"

        try:
            cursor.execute(query, (library.name, library.description, library.logo_url, library.coordinates))

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
    def set_library_hours(library_details):
        """
        Add / Update library info like open days, Time
        """
        conn = Database.db_connection()
        cursor = conn.cursor()

        check_hours = "SELECT * FROM Library_hours WHERE library_id = %s AND day_of_week = %s"
        add_hours = "INSERT INTO Library_hours (library_id, day_of_week, open_time, close_time) VALUES (%s, %s, %s, %s)"
        update_hours = "UPDATE Library_hours SET day_of_week = %s, open_time = %s, close_time = %s WHERE library_id = %s"

        try:
            cursor.execute(check_hours, (library_details.library_id, library_details.day_of_week))
            results = cursor.fetchall()
            if results:
                cursor.execute(update_hours, (library_details.day_of_week, 
                                          library_details.open_time, 
                                          library_details.close_time, 
                                          library_details.library_id))
                conn.commit()

            else:
                cursor.execute(add_hours, (library_details.library_id,
                                       library_details.day_of_week,
                                       library_details.open_time, 
                                       library_details.close_time
                                       ))
                conn.commit()
        except mysql.connector.Error as e:
            return {"success": False, "message": f"{e}"}
        
        else:
            if cursor.rowcount > 0:
                return {"success": True, "message": "Library hours have been updated!"}
            return {"success": False, "message": "No changes have been made"}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def edit_library_hours(id, library_details):
        conn = Database.db_connection()
        cursor = conn.cursor()

        check_hours = "SELECT * FROM Library_hours WHERE library_id = %s"
        update_hours = "UPDATE Library_hours SET day_of_week = %s, open_time = %s, close_time = %s WHERE library_id = %s AND day_of_week = %s"

        try:
            cursor.execute(check_hours, (id,))
            results = cursor.fetchall()
            if results:
                cursor.execute(update_hours, (library_details.day_of_week, 
                                          library_details.open_time, 
                                          library_details.close_time, 
                                          library_details.library_id,
                                          library_details.day_of_week
                                          ))
                conn.commit()

            else:
                cursor.execute(update_hours, (library_details.library_id,
                                       library_details.day_of_week,
                                       library_details.open_time, 
                                       library_details.close_time
                                       ))
                conn.commit()
        except mysql.connector.Error as e:
            return {"success": False, "message": f"{e}"}
        
        else:
            if cursor.rowcount > 0:
                return {"success": True, "message": "Library hours have been updated!"}
            return {"success": False, "message": "No changes have been made"}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def delete_hours(library_id, day_of_week):
        conn = Database.db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM Library_hours WHERE library_id = %s AND day_of_week = %s"

        try:
            cursor.execute(query, (library_id, day_of_week))
            cursor.fetchall()
            conn.commit()

        except mysql.connector.Error as err:
            return {"success": False, "message": f"{err}"}
        
        else:
            if cursor.rowcount > 0:
                return {"success": True, "message": f"Library hours for day {day_of_week} has been deleted."}
            return {"success": False, "message": "Oops! We ran into a problem"}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def delete_library(id):
        conn = Database.db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM Libraries WHERE id = %s"

        try:
            cursor.execute(query, (id,))

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ROW_IS_REFERENCED_2:
                return {"sucess": False, 
                        "message": "Error: Library could not be deleted. Clear library data first."}
            return {"success": False, "message": f"{err}"}
        
        else:
            conn.commit()
            if cursor.rowcount > 0:
                return {"success": True, "message": f"The Library has been succesfully deleted"}
            return {"success": False, "message": "The library you're trying to delete doea not exist!"}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def get_library(id):
        conn = Database.db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Libraries WHERE id = %s"
        
        try:
            cursor.execute(query, (id,))
            results = cursor.fetchall()
            
        except mysql.connector.Error as err:
            return {"success": False, "message": f"Error message: '{err}'"}
        
        else:
            if cursor.rowcount > 0:
                return {"success": True, "message": "Operation successful!", "data": results}
            return {"success": False, "message": "Library not found", "data": []}
        
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
            return {"success": False, "message": "No libraries.", "data": []}
        
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
        query = "UPDATE Libraries SET name = %s, description = %s, logo_url = %s, coordinates = %s WHERE id = %s"

        try:
            cursor.execute(query, (new_library_info.name, 
                                   new_library_info.description, 
                                   new_library_info.logo_url,
                                   new_library_info.coordinates, 
                                   library_id))
            
        except mysql.connector.Error as err:
            return {"success": False, "message": f"{err}"}
        
        else:
            conn.commit()
            if cursor.rowcount > 0:
                return {"success": True, "message": "Library updated successfully"}
            return {"success": False, "message": "Nothing has been updated. Enter your changes and save."}
        
        finally:
            Database.db_clean_up(conn, cursor)