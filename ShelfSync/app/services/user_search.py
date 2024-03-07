"""
Search users (employees and patrons)
"""

from .. import app
from flask import Flask, render_template, session, request
from ..utils.database import get_database_connection
import mysql.connector

def search_emplyoyee(keyword=None):

	"""
	Searches employees from DB

	Args:
	"""

	conn = get_database_connection()
	cursor = conn.cursor()

	if not keyword is None:

		query = "SELECT * FROM employee WHERE `name` LIKE %s"

		try:

			cursor.execute(query, ("%"+keyword+"%",))

			data = cursor.fetchall()

			if (cursor.rowcount > 0):

				return data
			else:

				return 0

		except mysql.connector.Error as err:

			return f"Error: {err}"

		finally:

			cursor.close()
			conn.close()
	else:

		query_all = "SELECT * FROM employee"

		try:

			cursor.execute(query_all)

			all_data = cursor.fetchall()

			if (cursor.rowcount > 0):

				return all_data
			else:

				return 0
		except mysql.connector.Error as err:

			return f"Error {err}"

		finally:
			cursor.close()
			conn.close()
