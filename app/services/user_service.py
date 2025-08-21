from app.extensions import Database
import mysql.connector
from mysql.connector import errorcode

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
    def get_users(user_type, library_id):
        conn = Database.db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Users WHERE role = %s AND library_id = %s"

        try:
            cursor.execute(query, (user_type, library_id))
            results = cursor.fetchall()

        except mysql.connector.Error as err:
            return {"success": False, "message": "Oops! We ran into a problem. Try again later."}
        
        else:
            if cursor.rowcount > 0:
                return {"success": True, "message": "Operation successful", "data": results}
            return {"success": True, "message": "No users", "data": []}

        finally:
            Database.db_clean_up(conn, cursor)        


    @staticmethod
    def update_user_info(new_user_info, user_id, library_id):
        conn = Database.db_connection()
        cursor = conn.cursor()
        query = "UPDATE Users SET name = %s, surname = %s, email = %s, phone = %s,  password_hash = %s WHERE" \
        " id = %s AND library_id = %s"

        try:
            cursor.execute(query, (new_user_info.name,
                                   new_user_info.surname,
                                   new_user_info.email,
                                   new_user_info.phone,
                                   new_user_info.password_hash,
                                   user_id,
                                   library_id))

        except mysql.connector.Error as err:
            return {"success": False, "message": f"Oops! We ran into a problem. Try again later."}
        
        else:
            conn.commit()
            if cursor.rowcount > 0:
                return {"seccess": True, "message": "personal details succesfully updated"}
            return {"success": False, "message": "Could not update personal information. Try again."}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def edit_user_profile(user):
        conn = Database.db_connection()
        cursor = conn.cursor()
        query = "UPDATE Users SET role = %s, is_active = %s WHERE id = %s AND email = %s"

        try:
            cursor.execute(query, (user.role, user.isactive, user.user_id, user.email))

        except mysql.connector.Error as err:
            return {"success": False, "message": f"Oops! We ran into a problem. Try again later."}
        
        else:
            conn.commit()
            if cursor.rowcount > 0:
                return {"success": True, "message": "Success!"}
            return {"success": True, "message": "Nothing to upate."}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def user_search(query_string, is_admin):
        conn = Database.db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Users WHERE (name LIKE %s OR surname LIKE %s) AND role = %s"

        try:
            cursor.execute(query, (f"%{query_string}%", f"%{query_string}%", is_admin))
            results = cursor.fetchall()

        except mysql.connector.Error as err:
            return {"success": False, "message": "Oops! We ran into a problem. Try again later", "data": ["Exception"]}
        
        else:
            if cursor.rowcount > 0:
                return {"success": True, "message": "Success!", "data": results}
            return {"success": True,  "message": "No match was found.", "data": []}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def sign_in():
        pass

    @staticmethod
    def sign_out():
        pass