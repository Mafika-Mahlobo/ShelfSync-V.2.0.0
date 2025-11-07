from flask import Blueprint, request, render_template, jsonify
from app.models.book import Books
from app.services.book_service import BookManager
from app.utils.helpers import Helpers


book_searchbp = Blueprint("search", __name__, url_prefix="/books")
booksbp = Blueprint("book", __name__, url_prefix="/book_add")

@booksbp.route("/")
def add_book():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    new_book = Books(**data)
    response = BookManager.add_book(new_book)
    return response["message"]

@book_searchbp.route("/<query>", methods=["GET"])
def book_search(query):
    return BookManager.get_books_info(query)
    

