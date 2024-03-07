"""
Entry point to the application.
"""

from flask import Flask, render_template, session, request, flash, redirect, url_for
from app import app
from app.utils.database import get_database_connection
from app.services.user_service import signin
from app.services.catalog_service import add_resource, delete_resource, view_resource
from app.services.patron_register import register
from app.services.employee_register import add_employee, update_employee_info, delete_employee_info
from app.services.user_search import search_emplyoyee
from app.models.search_resource import get_resource
import hashlib

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
<<<<<<< HEAD
		title = get_resource(search_key, 'title')
		pic = get_resource(search_key, 'imageLinks')
		book_id = get_resource(search_key, 'industryIdentifiers')
		description = get_resource(search_key, "description")
		return render_template("search_results.html", user=title, pic=pic, book_id=book_id, about=description)

=======
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
def get_patrons():
	pass

@app.route("/api/paron_register", methods=["POST"])
def register_patron():

	if request.method == "POST":
		md5_hash = hashlib.md5()

		name = request.form["name"]+" "+request.form["surname"]
		address = f"{request.form["address-line1"]}, {request.form["address-line2"]}, {request.form["address-line3"]}, {request.form["address-line4"]}"
		email = request.form["email"]
		phone_number = request.form["phone"]
		username = request.form["email"]
		password = request.form["password"]
		md5_hash.update(password.encode("utf-8"))
		hashed_password = md5_hash.hexdigest()

		response = register((name, address, email, phone_number, email, hashed_password, 0, 0))
		if response == 1:
			return render_template("index.html", sucess="Registration succesul")
		if (response == 0):
			return render_template("index.html", error="Registration failed")
		return render_template("index.html", error=response)

@app.route("/api/employee_register", methods=["POST"])
def register_user():

	if request.method == "POST":

		md5_hash = hashlib.md5()

		name =  f"{request.form["name"]} {request.form["surname"]}"
		possition =  request.form["position"]
		email =  request.form["email"]
		phone_number = request.form["phone"]
		username = request.form["email"]
		password = request.form["password"]

		if "toggleButton" in request.form:
			if request.form["toggleButton"] == "No":
				is_admin = 0
			else:
				is_admin = 1
		else:
			is_admin = 0

		md5_hash.update(password.encode("utf-8"))
		hashed_password = md5_hash.hexdigest()

		data = (name, possition, email, phone_number, username, hashed_password, is_admin)
		response = add_employee(data)

		if response == 1:
			return render_template("Admin.html", sucess="Employoyee succesully added ")
		return render_template("Admin.html", error="The email address is already registred")


@app.route("/api/user_search", methods=["POST"])
def search_user(user_keyword=None):

	if request.method == "POST":

		keyword = request.form["user_key"]

		response = search_emplyoyee(keyword)

		if (response == 0):

			return "No data found"
		else:

			return response

@app.route("/api/update_employee/<employee_info>", methods=["POST"])
def update_employee(employee_info):

	md5_hash = hashlib.md5()

	data = request.json

	name = f"{data["name"]} {data["surname"]}"
	position = data["position"]
	email = data["email"]
	phone_number = data["phone"]
	username = data["email"]
	is_admin = data["is_admin"]
	password = data["password"]

	md5_hash.update(password.encode("utf-8"))
	hashed_password = md5_hash.hexdigest()

	user_info = (name, position, email, phone_number, username, hashed_password, is_admin, email)

	response = update_employee_info(user_info) 

	if (response == 1):

		return render_template("Admin.html", sucess="Employoyee information updated")
	return render_template("Admin.html", error="Could not update employee informaotion")



@app.route("/api/delete_employee/<employee_id>", methods=["POST"])
def delete_employee(employee_id):

	data = request.json

	email = data["employee_id"]

	response = delete_employee_info(email)

	if request == 1:
		return render_template("Admin.html", sucess="Employee succesully removed")
	return render_template("Admin.html", error="Could not delete employee")


@app.route("/api/local_books/<key_word>", methods=["POST"])
def get_books_transaction(key_word=None):

	data = request.json

	key = data["key_word"]

	response = view_resource(key)

	if (response == 0):
		return "No books found"
	return response 
>>>>>>> resourceLogic



if __name__ == "__main__":
	app.run(debug=True)