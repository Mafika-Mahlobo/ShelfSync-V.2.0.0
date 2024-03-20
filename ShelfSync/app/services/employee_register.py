"""
Registers emplyoyee
"""

from .. import app
from flask import Flask, render_template, session, request
from ..utils.database import get_database_connection
import mysql.connector

def add_employee(employee_info):
	
	"""
	Adds user to the database.

	Args:
		umployee information (tuple): tuple containing employee information.

	Returns:
		int/str: status code or error from DB. 1 for success, 0 for failure
	"""

	conn = get_database_connection()
	cursor = conn.cursor() 

	check_query = "SELECT * FROM employee WHERE `email` = %s"
	query = "INSERT INTO employee (name, position, email, phone, username, password, is_admin) VALUES (%s, %s, %s, %s, %s, %s, %s)"

	try:

		cursor.execute(check_query, (employee_info[2],))

		existing_user = cursor.fetchall()

		if existing_user:
			conn.close()
			return "User already registered"

		cursor.execute(query, employee_info)

		conn.commit()

		if (cursor.rowcount > 0):
			return 1
		return 0

	except mysql.connector.Error as err:

		return f"Error: {err}"



def update_employee_info(employee_info):

	"""
	Update user information

	Args:
		umployee information (tuple): tuple containing employee information.

	Returns:
		int/str: status code or error from DB. 1 for success, 0 for failure.
	"""

	conn = get_database_connection()
	cursor = conn.cursor()


	query = "UPDATE employee SET `name` = %s, `position` = %s, `email` = %s, `phone` = %s, `username` = %s, `password` = %s, `is_admin` = %s WHERE `email` = %s"

	try:

		cursor.execute(query, employee_info)

		conn.commit()

		if (cursor.rowcount > 0):

			return 1
		return 0

	except mysql.connector.Error as err:

		return f"Error: {err}"

	finally:

		cursor.close()
		conn.close()



def delete_employee_info(employee_id):

	"""
	deletes user from DB

	Args:
		umployee id (str): tuple containing employee information.

	Returns:
		int/str: status code or error from DB. 1 for success, 0 for failure
	"""

	conn = get_database_connection()
	cursor = conn.cursor()

	query = "DELETE FROM employee WHERE `email` = %s"

	try:

		cursor.execute(query, (employee_id,))

		conn.commit()

		if (cursor.rowcount > 0):
			return 1
		return 0

	except mysql.connector.Error as err:

		return f"Error: {err}"

	finally:
		cursor.close()
		conn.close()


