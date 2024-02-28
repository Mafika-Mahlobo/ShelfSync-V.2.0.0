"""
Resource management module (Add, Edit, Delete)
"""

from flask import Falsk, render_template, session, resquest
from .. import app
from ..utils.database import get_database_connection
from ..api.external_api import 

conn = get_database_connection()
cursor = conn.cursor()

def resource_add(book):
	"""
	Adds resource to DB

	....
	"""
	
	isbn_number = book["industryIdentifiers"]
	book_title = book["title"]
	authors = str(book["authors"])
	publisher = book["publisher"]
	published_date = book["publishedDate"]
	description = book["description"]
	categories = book["categories"]
	language = book["language"]
	link1 = book["imageLinks"]["'smallThumbnail"]
	link2 = ["thumbnail"]
	thumbnails = str(link1)+","+str(link2)

	sql = "INSERT INTO resources (isbn, title, authors, publisher, published_date, description, categories, language, url) VALUES (isbn_number, book_title, authors, publisher, published_date, description, categories, language, thumbnails)"

	try:
		query = cursor.execute(sql)
		if (query is not None):
			return 1
		else:
			return 0
			
def resource_edit():

	"""
	Edits information about resource.

	...
	"""
	pass

def resource_delete():

	"""
	Removes resource from DB.

	...
	"""
	pass