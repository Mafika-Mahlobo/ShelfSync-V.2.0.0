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
	vid_path = "app/static/media/img/"
	return render_template("index.html", vid=vid_path)



@app.route("/signin")
def login():
	username = "Admin1"
	password = "Admin123" #get credentials from front-end (HTML)
	return signin(username, password)

	
@app.route("/signout")
def logout():
	session.clear()
	return render_template("index.html")


#Main page book search
@app.route("/api/resources", methods=["POST"])
def search():

	if (request.method == "POST"):
		search_key = request.form["key_word"]
		title = get_resource(search_key, 'title')
		pic = get_resource(search_key, 'imageLinks')
		book_id = get_resource(search_key, 'industryIdentifiers')
		description = get_resource(search_key, "description")
		return render_template("search_results.html", user=title, pic=pic, book_id=book_id, about=description)




if __name__ == "__main__":
	app.run(debug=True)
