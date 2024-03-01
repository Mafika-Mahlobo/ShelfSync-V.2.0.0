"""
Entry point to the application.
"""

from flask import Flask, render_template, session, request
from app import app
from app.utils.database import get_database_connection
from app.services.user_service import signin
from app.models.search_resource import get_resource

app.config.from_pyfile("config.py")
app.secret_key = "078127ABC"


@app.route('/')
def index():
	img = "app/static/media/img/"
	return render_template("index.html", vid=img)



@app.route("/api/signin", methods=["POST"])
def login():
	if (request.method == "POST"):
		username = request.form["username"]
		password = request.form["password"]
		return signin(username, password)
	return "Could not sign you in."

	
@app.route("/signout")
def logout():
	session.clear()
	return render_template("index.html")


#Main page book search
@app.route("/api/search", methods=["POST"])
def search():

	if (request.method == "POST"):
		search_key = request.form["key_word"]
		data = get_resource(search_key)
		return render_template("search_results.html", volume=data)

#add book
@app.route("/api/resources/{resource_id}")
def add_book():

	pass

@app.route("/api/navigate")
def menu_navigate():
	pass



if __name__ == "__main__":
	app.run(debug=True)