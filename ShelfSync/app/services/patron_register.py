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

	query = "INSERT INTO patrons (`name`, `address`, `email`, `phone`, `username`, `password`, `credit`, `debit`) VALUES (%s, %s, %s, %s, %s, %d, %d, %d)"

	try:

		response = cursor.execute(query, patron_info)

		conn.commit()

		if (response.rowcount > 0):
			return "Registation processed"
		return "Registration failed"

	except mysql.connector.Error as err:
		return err





