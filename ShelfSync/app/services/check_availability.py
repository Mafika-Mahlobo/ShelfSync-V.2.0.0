"""
Checks book avalability
"""

from flask import Flask, render_template, session, request
from .. import app
from ..utils.database import get_database_connection
import mysql.connector

def book_availability(book_id):

	"""
	Checks if book is available for lending.

	Args:
	"""

	conn = get_database_connection()
	cursor = conn.cursor()

	query = "SELECT * FROM transactions WHERE `isbn` = %s"

	try:

		cursor.execute(query, (book_id,))

		cursor.fetchall()

		if (cursor.rowcount > 0):
			return 0
		return 1

	except mysql.connector.Error as err:

		return f"Error: {err}"

	finally:

		cursor.close()
		conn.close()