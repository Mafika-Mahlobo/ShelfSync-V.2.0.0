"""
Module for handling user related logic
"""

from flask import Flask, render_template, session, request
from .. import app
from ..utils.database import get_database_connection

app.secret_key = "078127ABC"

def signin(username, password):

	db = get_database_connection()
	cursor = db.cursor()
	try:
		
		cursor.execute("SELECT * FROM  employee WHERE username = username AND password = password")

		user_data = cursor.fetchall()

		if (len(user_data) > 0):
			session["id"] = user_data[0][0]
			session["username"] = user_data[0][5]
			session["isAdmin"] = user_data[0][7]

			username = session.get("username")
			isadmin_str = session.get("isAdmin")

			isadmin = isadmin_str == True

			if (isadmin):
				return render_template("Admin.html", username=username)
			else:
				return render_template("Employee.html", username=username)
		return render_template("index.html", error="Ivalid username or password")

	except Exception as e:

		return render_template("index.html", error=e)

	finally:
		cursor.close()
		db.close()
	