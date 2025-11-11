from app.models.transaction import Loans, Fines
import mysql.connector
from app.extensions import Database
import datetime

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
                    datetime.datetime.now(),
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

    @staticmethod
    def check_in(loan_id):
        conn = Database.db_connection()
        cursor = conn.cursor()

        get_loan = "SELECT book_id, status FROM Loans WHERE id = %s"
        update_loan = "UPDATE Loans SET returned_at = NOW(), status = %s WHERE id = %s"
        update_resource = "UPDATE Books SET available_copies = available_copies + 1 WHERE book_id = %s"

        try:
            cursor.execute(get_loan, (loan_id,))
            response = cursor.fetchone()
            if response and response[1] == LOAN_STATUS[0]:
                book_id = response[0]
                cursor.execute(update_loan, (LOAN_STATUS[1], loan_id))
                cursor.execute(update_resource, (book_id,))
                conn.commit()
            else:
                return {"success": False, "message": "Invalid loan ID or the book has already been returned."}

        except mysql.connector.Error as err:
            return {"success": False, "message": f"e{err}"}
        
        else:
            return {"success": True, "message": f"The loan ID: {loan_id} has been successfully checked in."}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def filter_loans(user_id):
        conn = Database.db_connection()
        cursor = conn.cursor(dictionary=True)

        get_loans = "SELECT * FROM Loans WHERE user_id = %s"

        try:
            cursor.execute(get_loans, (user_id,))
            loans = cursor.fetchall()
            if loans:
                return {"success": True, "data": loans}
            else:
                return {"success": False, "message": "No loans found for the specified user."}

        except mysql.connector.Error as err:
            return {"success": False, "message": f"e{err}"}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def list_all_loans():
        conn = Database.db_connection()
        cursor = conn.cursor(dictionary=True)

        get_loans = "SELECT * FROM Loans"

        try:
            cursor.execute(get_loans)
            loans = cursor.fetchall()
            if loans:
                return {"success": True, "data": loans}
            else:
                return {"success": False, "message": "No loans found for the specified user."}

        except mysql.connector.Error as err:
            return {"success": False, "message": f"e{err}"}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def list_fines(user_id):
        conn = Database.db_connection()
        cursor = conn.cursor(dictionary=True)

        get_fines = "SELECT * FROM Fines WHERE user_id = %s"

        try:
            cursor.execute(get_fines, (user_id,))
            fines = cursor.fetchall()
            if fines:
                return {"success": True, "data": fines}
            else:
                return {"success": False, "message": "No fines found for the specified user."}

        except mysql.connector.Error as err:
            return {"success": False, "message": f"e{err}"}
        
        finally:
            Database.db_clean_up(conn, cursor)

    @staticmethod
    def issue_fine(loan_id):
        conn = Database.db_connection()
        cursor = conn.cursor()

        check_fine = "SELECT id FROM Fines WHERE loan_id = %s AND paid = %s"
        issue_fine = "INSERT INTO Fines (user_id, loan_id, amount, paid, issued_at, paid_at) \
                      VALUES ((SELECT user_id FROM Loans WHERE id = %s), %s, %s, %s, NOW(), %s)"
        update_amaunt = "UPDATE Fines SET amount = amount + %s WHERE loan_id = %s AND paid = %s"
        update_Loans = "UPDATE Loans SET due_date = %s WHERE id = %s"
        

        fine_amount = 10.00  # Example fixed fine amount

        try:
            cursor.execute(check_fine, (loan_id, False))
            response = cursor.fetchone()
            if response:
                cursor.execute(update_amaunt, (fine_amount, loan_id, False))
            else:
                cursor.execute(issue_fine, (
                    loan_id,
                    loan_id,
                    fine_amount,
                    False,
                    None
                ))
                cursor.execute(update_Loans, (
                    datetime.datetime.now() + datetime.timedelta(days=7),
                    loan_id
                ))
            conn.commit()

        except mysql.connector.Error as err:
            return {"success": False, "message": f"e{err}"}
        
        else:
            return {"success": True, "message": f"A fine of ${fine_amount} has been issued for loan ID: {loan_id}."}
        
        finally:
            Database.db_clean_up(conn, cursor)
