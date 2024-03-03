"""
Entry point to the application.
"""

from flask import Flask, render_template, session, request
from app import app
from app.utils.database import get_database_connection
from app.services.user_service import signin
from app.services.catalog_service import add_resource, delete_resource
from app.services.patron_register import register
from app.models.search_resource import get_resource

app.config.from_pyfile("config.py")
app.secret_key = "078127ABC"


@app.route('/')
def index():
	
	img = "app/static/media/img/"
	if "username" in session:
		return render_template('Admin.html', error="Your session is still on. sign-out before closing")
	else:
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

		if "username" in session:
			return render_template("Add_book.html", volume=data)
		else:
			return render_template("search_results.html", volume=data)


#add book
@app.route("/api/resources", methods=["POST"])
def search_book():

	if request.method == "POST":
		return render_template("Add_book.html")

			

@app.route("/api/resources/<resource_id>", methods=["POST"])
def add_book(resource_id):

	data = get_resource(resource_id)
	query_status = add_resource(data)

	if not query_status is None:
		return render_template("Add_book.html", sucess=query_status)
	else:
		return render_template("Add_book.html", error=query_status)


@app.route("/api/resources_delete", methods=["POST"])
def delete_book():
	
	if request.method == "POST":
		resource_id = request.form["book_id"]
		response = delete_resource(resource_id)
		return render_template("Admin.html", error=response)

	else:
		return render_template("Admin.html", error="error")


@app.route("/api/resources/<resource_id>}", methods=["PUT"])
def update_book_info(resource_id):
	pass


@app.route("/api/patrons", methods=["POST"])
def register_patron():
	pass


if __name__ == "__main__":
	app.run(debug=True)