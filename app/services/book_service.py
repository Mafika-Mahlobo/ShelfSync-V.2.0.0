"""
Book Services
"""
from app.utils.helpers import Helpers
from app.models.book import Books
from app.extensions import Database
import mysql.connector
import json

class BookManager:

    @staticmethod
    def get_books_info(search_string):
        return Helpers.books_info(search_string)
    
    @staticmethod
    def add_book(book):
        conn = Database.db_connection()
        cursor = conn.cursor()
        check_query = "SELECT library_id, total_copies FROM Books WHERE isbn = %s AND library_id = %s"
        check_library = "SELECT * FROM Libraries WHERE id = %s"
        add_query = "INSERT INTO Books (library_id, title, description, image_link, isbn, categories, authors, total_copies, available_copies) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        add_copy_query = "UPDATE Books SET total_copies = %s WHERE isbn = %s AND library_id = %s"
        
        try:

            cursor.execute(check_query, (book.isbn, book.library_id))
            results = cursor.fetchone()

            if results:
                total = int(results[1]) + 1
                cursor.execute(add_copy_query, (total, book.isbn, book.library_id))
                conn.commit()

                if cursor.rowcount > 0:
                    return {"success": True, "message": f"Success! TThere now {total} copies of resource ID: {book.isbn}."}

            else:
                cursor.execute(check_library, (book.library_id,))
                library_exits = cursor.fetchone()
                if library_exits:

                    cursor.execute(add_query, ( 
                                    book.library_id, 
                                    book.title,
                                    book.description,
                                    book.image_link,
                                    book.isbn,
                                    json.dumps(book.authors),
                                    json.dumps(book.category),
                                    book.total_copies,
                                    book.available_copies))
                    conn.commit()
                else:
                    return {"success": False, "message": f"Library ID: {book.library_id} does not exits!"}
                
        except mysql.connector.Error as e:
            return {"success": False, "message": f"Error message: {e}"}
        
        else:
            if cursor.rowcount > 0:
                return {"success": True, "message": f"success! Resource ID {book.isbn} has been added."}
            return {"success": False, "message": "Sorry. We could not add the resource. Try again later"}
        
        finally:
            Database.db_clean_up(conn, cursor)