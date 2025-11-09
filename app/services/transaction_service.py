from app.models.transaction import Loans, Fines
import mysql.connector
from app.extensions import Database

LOAN_STATUS = ["borrowed", "returned", "overdue", "cancelled"]

class TransactionManager:

    @staticmethod
    def check_out(resource_id, loan_information):
        conn = Database.db_connection()
        cursor = conn.cursor()

        check_resource = "SELECT available_copies FROM Books WHERE book_id = %s"
        add_loan = "INSERT INTO Loans (user_id, book_id, library_id, borrowed_at, due_date, returned_at, status) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"
        update_resource = "UPDATE Books SET available_copies = %s WHERE book_id = %s"

        try:
            cursor.execute(check_resource, (resource_id,))
            response = cursor.fetchone()
            if response:
                cursor.execute(add_loan, (
                    loan_information.user_id,
                    resource_id,
                    loan_information.library_id,
                    loan_information.borrowed_at,
                    loan_information.due_date,
                    loan_information.returned_at,
                    LOAN_STATUS[0]
                ))
                copies = int(response[0]) - 1
                cursor.execute(update_resource, (copies, resource_id))
                conn.commit()

            else:
                return {"success": False, "message": "The resource is not available for lending"}

        except mysql.connector.Error as err:
            return {"success": False, "message": f"e{err}"}
        
        else:
            return {"success": True, "message": f"The resource, ID: {resource_id} \
                    has been landed. Return date is {loan_information.due_date}. {copies} copies left."}
        
        finally:
            Database.db_clean_up(conn, cursor)
