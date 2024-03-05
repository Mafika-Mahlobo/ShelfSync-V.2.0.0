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
			return "Registration processed"
		return "Registration failed"

	except mysql.connector.Error as err:

		return f"Error: {err}"
