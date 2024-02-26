"""
Entry point to the application.
"""

from flask import Flask, render_template, session, request
from app import app
from app.utils.database import get_database_connection
from app.services.user_service import signin

app.config.from_pyfile("config.py")
app.secret_key = "078127ABC"


@app.route('/')
def index():
	db = get_database_connection()
	cursor = db.cursor()
	cursor.execute("SELECT * FROM resource")
	data = cursor.fetchall()
	return render_template("index.html", user=data)
	cursor,close()
	db.close()



@app.route("/signin")
def login():
	#username = "Admin1"
	#password = "Admin123" get credentials from front-end (HTML)
	return signin(username, password)

	
@app.route("/signout")
def logout():
	session.clear()
	return render_template("index.html")



if __name__ == "__main__":
	app.run(debug=True)
