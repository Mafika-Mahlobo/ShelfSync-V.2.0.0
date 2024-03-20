"""
Processes transaction
"""

from flask import Flask, render_template, session, request
from .. import app
from ..utils.database import get_database_connection
import mysql.connector

def checkout(transaction_data):

	"""
	Processes checkout transactions

	Args:
		transaction_data (tuple): A tuple of transaction data like date, isbn etc.

	Returns:
		int: one for success, zero for failure
	"""

	conn = get_database_connection()
	cursor = conn.cursor()


	check_query = "SELECT * FROM `transactions` WHERE `isbn` = %s"

	query = "INSERT INTO `transactions` (isbn, employee_id, patron_id, transaction_type, transaction_date, due_date, fee) VALUES (%s, %s, %s, %s, %s, %s ,%s)"

	try:

		cursor.execute(check_query, (transaction_data[0],))
		existing = cursor.fetchall()
		if existing:
			conn.close()
			return "Book already checked out"

		cursor.execute(query, transaction_data)
		conn.commit()

		if (cursor.rowcount > 0):

			return 1
		return 0

	except mysql.connector.Error as err:

		return f"Error: {err}"

	finally:
		cursor.close()
		conn.close()


def checkin(isbn):

	"""
	Processes chekin transaction

	Args:
		isbn number (str): unique identifier for a book

	Returns:
		int: one for success and zero for failure.

	"""

	conn = get_database_connection()
	cursor = conn.cursor()

	check_query = "SELECT * FROM `transactions` WHERE `isbn` = %s"
	query =  "DELETE FROM `transactions` WHERE `isbn` = %s"

	try:

		cursor.execute(check_query, (isbn,))
		exists = cursor.fetchall()

		if not exists:
			conn.close()
			return "Book already on the system"

		cursor.execute(query, (isbn,))
		conn.commit()

		if (cursor.rowcount > 0):
			return 1
		return 0

	except mysql.connector.Error as err:

		return f"Error: {err}"

	finally:

		cursor.close()
		conn.close()