"""
Module for handling user related logic


Notes:
	this is for employee sign-in. change name.
"""


from flask import Flask, render_template, session, request
from .. import app
from ..utils.database import get_database_connection
import hashlib

app.secret_key = "078127ABC" # move to database file to avoid duplicating

def signin(username, password):

	"""
	Authenticate and open session for user

	.....
	"""

	md5_hash = hashlib.md5()
	md5_hash.update(password.encode("utf-8"))
	hashed_password = md5_hash.hexdigest()

	db = get_database_connection()
	cursor = db.cursor()
	try:
		
		query = "SELECT * FROM employee WHERE `username` = %s COLLATE utf8mb4_bin AND `password` = %s COLLATE utf8mb4_bin"
		cursor.execute(query, (username, hashed_password))

		user_data = cursor.fetchall()

		if (len(user_data) == 1):
			session["id"] = user_data[0][0]
			session["username"] = user_data[0][5]
			session["isAdmin"] = user_data[0][7]

			user = request.form["username"]
			isadmin_flag = session.get("isAdmin")

<<<<<<< HEAD
			

			if (isadmin_str == 1):
				return render_template("Admin.html", username=username)
=======
			if (isadmin_flag == 1):
				return render_template("Admin.html", username=username, path='../static/iframe_pages/home.html')
>>>>>>> resourceLogic
			else:
				return render_template("Employee.html", username=username)

		elif (len(user_data) < 1):

			return render_template("index.html", error="Ivalid username or password")

		else:

			return render_template("index.html", error="There was an isuue logging you in. multiple entries in the database.")

	except Exception as e:

		return render_template("index.html", error=e)

	finally:
		cursor.close()
		db.close()
	