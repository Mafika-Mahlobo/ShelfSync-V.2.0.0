"""
Entry point to the application.
"""

from flask import Flask, render_template, session, request
from app import app
from app.utils.database import get_database_connection

app.config.from_pyfile('config.py')
#app.secret_key = read from file


@app.route('/')
def index():
	db = get_database_connection()
	cursor = db.cursor()
	cursor.execute("SELECT * FROM resource")
	data = cursor.fetchall()
	return render_template('index.html', user=data)
	cursor,close()
	db.close()


# User sign In
@app.route('/signin')
def login():

	username = request.form["username"]
	password = request.form["password"]

	db = get_database_connection()
	cursor = db.cursor()
	try:
		
		cursor.execute("SELECT * FROM  employee WHERE username = username AND password = password")

		user_data = cursor.fetchall()

		if (len(user_data) > 0):
			session["id"] = user_data[0][0]
			session["name"] = user_data[0][1]
			session["position"] = user_data[0][2]
			session["email"] = user_data[0][3]
			session["phone"] = user_data[0][4]
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

@app.route("/signout")
def logout():
	session.clear()
	return render_template("index.html")



if __name__ == "__main__":
	app.run(debug=True)
