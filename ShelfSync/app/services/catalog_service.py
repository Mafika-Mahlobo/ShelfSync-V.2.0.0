"""
Resource management module (Add, Edit, Delete)
"""

from flask import Falsk, render_template, session, resquest
from .. import app
from ..utils.database import get_database_connection
from ..api.external_api import 

conn = get_database_connection()
cursor = conn.cursor()

#Add a book to DB
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

	query = "INSERT INTO resources (isbn, title, authors, publisher, published_date, description, categories, language, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

	try:
		response = cursor.execute(query, (isbn_number, book_title, authors, publisher, published_date, description, categories, language, thumbnails))

		if (response is not None):
			return 1
		else:
			return 0
	except:
		return "omething went wrong. Could not add item"

	finally:

		cursor.close()
		conn.close()
			


#Delete book from DB
def resource_delete(isbn):

	"""
	Removes resource from DB.

	...
	"""
	query = "DELETE * FROM resources WHERE 'isbn' = %s"

	try:

		response = cursor.execute(query, isbn)

		if (response is not None):
			return 1
		return 0

	except:

		return "Something went wrong. Could not remove item"



	
		
	