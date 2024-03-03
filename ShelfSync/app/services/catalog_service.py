"""
Resource management module (Add, Edit, Delete)
"""

from flask import Flask, render_template, session, request
from .. import app
from ..utils.database import get_database_connection
import mysql.connector

#Add a book to DB
def add_resource(book):
	"""
	Adds resource to DB

	....
	"""
	conn = get_database_connection()
	cursor = conn.cursor()
	
	
	isbn_number = book[0]["industryIdentifiers"][0].get('identifier', '') if book and book[0].get("industryIdentifiers") else ''
	book_title = book[0]["title"]
	language = book[0]["language"]

	query = "INSERT INTO resources (isbn, title, language) VALUES (%s, %s, %s)"

	try:
		response = cursor.execute(query, (isbn_number, book_title, language))

		conn.commit()

		if (cursor.rowcount > 0):
			return "Book added"
		else:
			return "Error. Book not added"

	except mysql.connector.Error as err:
		return err

	finally:

		cursor.close()
		conn.close()
			


#Delete book from DB
def delete_resource(isbn):

	"""
	Removes resource from DB.

	...
	"""
	query = "DELETE * FROM resources WHERE 'isbn' = %s"

	try:

		cursor.execute(query, (isbn))

		if (cursor.rowcount > 0):
			return 1
		return 0

	except:

		return "Something went wrong. Could not remove item"