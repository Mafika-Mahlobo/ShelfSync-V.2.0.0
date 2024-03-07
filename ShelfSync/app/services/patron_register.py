"""
Module to register patrons
"""

from .. import app
from flask import Flask, render_template, session, request
from ..utils.database import get_database_connection
import mysql.connector

app.secret_key = "078127ABC" # move to database file to avoid duplicating

def register(patron_info):
	"""
	Registers patron to database.

	Args:

	"""

	conn = get_database_connection()
	cursor = conn.cursor()

	check_query = "SELECT * FROM patrons WHERE `email` = %s"

	cursor.execute(check_query, (patron_info[2],))

	existing_user = cursor.fetchall()

	if existing_user:
		cursor.close()
		return "User aleady registered"

	query = "INSERT INTO patrons (`name`, `address`, `email`, `phone`, `username`, `password`, `credit`, `debit`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

	try:

		response = cursor.execute(query, (patron_info))

		conn.commit()

		if (cursor.rowcount > 0):
			return 1
		return 0

	except mysql.connector.Error as err:
		return err

	finally:
		cursor.close()
		conn.close()




