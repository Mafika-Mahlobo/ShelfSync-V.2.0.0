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
    def book_web_search(search_string):
        return Helpers.books_info(search_string)
    
    @staticmethod
    def add_book(book, library_id):
        conn = Database.db_connection()
        cursor = conn.cursor()
        check_query = "SELECT library_id, total_copies, available_copies FROM Books WHERE isbn = %s AND library_id = %s"
        check_library = "SELECT * FROM Libraries WHERE id = %s"
        add_query = "INSERT INTO Books (library_id, authors, categories, description, book_id,  image_link, isbn, title, total_copies, available_copies) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        add_copy_query = "UPDATE Books SET total_copies = %s, available_copies = %s WHERE isbn = %s AND library_id = %s"
        
        try:

            cursor.execute(check_query, (book.isbn, library_id))
            results = cursor.fetchone()

            if results:
                total = int(results[1]) + 1
                available = int(results[2]) + 1
                cursor.execute(add_copy_query, (total, available, book.isbn, library_id))
                conn.commit()

                if cursor.rowcount > 0:
                    return {"success": True, "message": f"Success! TThere now {total} copies of resource ID: {book.isbn}."}

            else:
                cursor.execute(check_library, (library_id,))
                library_exits = cursor.fetchone()
                if library_exits:
                    total_copies = 1
                    available_copies = 1
                    cursor.execute(add_query, ( 
                                    library_id, 
                                    json.dumps(book.authors),
                                    json.dumps(book.category),
                                    book.description,
                                    book.book_id,
                                    json.dumps(book.image_link),
                                    book.isbn,
                                    book.title,
                                    total_copies,
                                    available_copies))
                    conn.commit()
                else:
                    return {"success": False, "message": f"Library ID: {library_id} does not exits!"}
                
        except mysql.connector.Error as e:
            return {"success": False, "message": f"Error message: {e}"}
        
        else:
            if cursor.rowcount > 0:
                return {"success": True, "message": f"success! Resource ID {book.isbn} has been added."}
            return {"success": False, "message": "Sorry. We could not add the resource. Try again later"}
        
        finally:
            Database.db_clean_up(conn, cursor)