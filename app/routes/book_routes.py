from flask import Blueprint, request, render_template, jsonify
from app.models.book import Books
from app.services.book_service import BookManager
from app.utils.helpers import Helpers

booksbp = Blueprint("book", __name__, url_prefix="/books")

@booksbp.route("/add/<library_id>", methods=["POST"])
def add_book(library_id):
    if request.is_json:
        data = request.get_json() 
    else:
        data = request.form.to_dict()

    field_map = {
    "isbn_number": "isbn",
    "id": "book_id",
    "images": "image_link",
    "categories": "category"
    }

    mapped_data = {field_map.get(k, k): v for k, v in data.items()}
    
    new_book = Books(**mapped_data)
    response = BookManager.add_book(new_book, library_id)
    return response["message"]

@booksbp.route("/search/<query>", methods=["GET"])
def book_search(query):
    return BookManager.book_web_search(query)
    

