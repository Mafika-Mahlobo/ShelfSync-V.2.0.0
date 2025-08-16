from app.extensions import Database
import mysql.connector
from app.config import User_role

class UserManager:
    
    @staticmethod
    def save_to_db(user):
        if not user == ():
            conn = Database.db_connection()
            cursor = conn.cursor()

            query = f"INSERT INTO `Users` (library_id, name, surname, email, phone, password_hash, role, is_active) VALUES \
            ('{user[0]}', '{user[1]}', '{user[2]}', '{user[3]}', '{user[4]}', '{user[5]}', '{user[6]}', '{user[7]}')"

            try:
                cursor.execute(query)

            except mysql.connector.Error as e:
                return f"Error: {e}"
            
            else:

                conn.commit()
                if cursor.rowcount > 0:
                    return True
                return False
            finally:

                Database.db_clean_up(conn, cursor)
              
        return False

    @staticmethod
    def get_patron(patron):
        pass

    @staticmethod
    def get_Admin(admin):
        pass

    @staticmethod
    def update_patron(patron):
        pass

    @staticmethod
    def update_admin(admin):
        pass

    @staticmethod
    def suspend_patron(patron):
        pass

    @staticmethod
    def suspend_admin(admin):
        pass

    @staticmethod
    def delete_user(user):
        pass