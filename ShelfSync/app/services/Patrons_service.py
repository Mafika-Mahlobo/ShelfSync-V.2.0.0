from flask import Flask, render_template, session, request
from .. import app
from ..utils.database import get_database_connection
import mysql.connector

def get_patreon():


	conn = get_database_connection()
	cursor = conn.cursor()

	query = "SELECT * FROM patrons"

	try:

		cursor.execute(query)

		data = cursor.fetchall();

		if (cursor.rowcount > 0):

			return data

		return 0

	except mysql.connector.Error as err:

		return f"Error: {err}"

	finally:

		cursor.close()
		conn.close()