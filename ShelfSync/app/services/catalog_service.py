"""
Resource management module (Add, Edit, Delete)
"""

from flask import Flask, render_template, session, request
from .. import app
from ..utils.database import get_database_connection
import mysql.connector


def add_resource(book):
	"""
	Adds resource to DB
	
	Args:
		Book (list): a list of dictionaries with book metadata

	Returns:
		int/str: status code or error message form DB. 1 for sucess, 0 for failure
	"""

	conn = get_database_connection()
	cursor = conn.cursor()
	
	
	isbn_number = book[0]["industryIdentifiers"][0].get('identifier', '') if book and book[0].get("industryIdentifiers") else ''
	book_title = book[0].get('title', '') if book and book[0].get("title") else ''
	language = book[0].get('language') if book and book[0].get('language') else ''

	query = "INSERT INTO resources (isbn, title, language) VALUES (%s, %s, %s)"

	try:
		response = cursor.execute(query, (isbn_number, book_title, language))

		conn.commit()

		if (cursor.rowcount > 0):
			return 1
		return 0

	except mysql.connector.Error as err:
		return f"Error: {err}"

	finally:

		cursor.close()
		conn.close()
			


def delete_resource(isbn):

	"""
	Removes resource from DB.

	Args:
		isbn (str): unique indentifier for a book

	Returns:
		int/str: Status code or DB error. 1 for success, 0 for failure.
	"""

	conn = get_database_connection()
	cursor = conn.cursor()

	query = "DELETE FROM resources WHERE `isbn` = %s"

	try:

		response = cursor.execute(query, (str(isbn),))

		conn.commit()

		if cursor.rowcount > 0:
			return 1
		return 0

	except mysql.connector.Error as err:

		return f"System Error: {err}" 

	finally:
		cursor.close()
		conn.close()


def view_resource(keyword=None):

	"""
	Searches internal catalog based on keyword

	Args:
		keyword (str): a search string

	Returns:
		List: List of tuple containing information from DB.
	 """

	conn = get_database_connection()
	cursor = conn.cursor()

	if not keyword is None:


		query = "SELECT * FROM resources WHERE `isbn` LIKE %s OR `title` LIKE %s"

		try:

			cursor.execute(query, ("%"+keyword+"%", "%"+keyword+"%"))

			data = cursor.fetchall()

			if (cursor.rowcount > 0):
				return data
			return 0

		except mysql.connector.Error as err:

			return f"Errror: {err}"

		finally:
			cursor.close()
			conn.close()
	else:

		query_all = "SELECT * FROM resources"

		try:

			cursor.execute(query_all)

			data_all = cursor.fetchall()

			if (cursor.rowcount > 0):
				return data
			return 0

		except mysql.connector.Error as err:

			return f"Error: {err}"