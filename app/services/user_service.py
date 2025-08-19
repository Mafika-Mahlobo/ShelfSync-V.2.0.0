from app.extensions import Database
import mysql.connector
from mysql.connector import errorcode
from app.config import User_role

class UserManager:

    @staticmethod
    def save_to_db(user):
        conn = Database.db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO `Users` (library_id, name, surname, email, phone, password_hash, role, is_active) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 

        try:
            cursor.execute(query, (user.library_id, 
                                   user.name, 
                                   user.surname, 
                                   user.email, 
                                   user.phone, 
                                   user.password_hash, 
                                   user.role, 
                                   user.isactive))

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                return {"sucess": False, "message": "Error: This user already exists."}
            
            if err.errno == errorcode.ER_NO_REFERENCED_ROW_2:
                return {"success": False, "message": "Could not add user. Select a library."}
            
            return {"success": False, "message": "Oops! We ran into a problem."}
            
        else:
            conn.commit()
            if cursor.rowcount > 0:
                return {"sucess": True, "message": f"Registration successful."}
            return {"success": False, "message": "Oops! We ran into a problem."}
        
        finally:
            Database.db_clean_up(conn, cursor)


    @staticmethod
    def delete_user(user):
        conn = Database.db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Users WHERE library_id = %s AND email = %s"

        try:
            cursor.execute(query, (user.library_id, user.email))

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ROW_IS_REFERENCED_2:
                return {"success": False, "message": "Cannot delete user. Delete user Loans first."}
            return {"success": False, "message": f"{err}"}
        
        else:
            conn.commit()
            if cursor.rowcount > 0:
                return {"success": True, "message": "The user has been successfully deleted."}
            return {"success": False, "message": "Could not find the specifies user"}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def get_patron():
        pass

    @staticmethod
    def get_Admin():
        pass

    @staticmethod
    def update_patron():
        pass

    @staticmethod
    def update_admin():
        pass

    @staticmethod
    def suspend_patron():
        pass

    @staticmethod
    def suspend_admin():
        pass