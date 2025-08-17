from flask import Blueprint, request, render_template, jsonify
from app.models.book import Books
from app.services.book_service import BookManager

booksbp = Blueprint("book", __name__, url_prefix="/add_book")
book_searchbp = Blueprint("search", __name__, url_prefix="/search_book")

@booksbp.route("/")
def add_book():
    new_book = Books(1, "New", "52773637", "fantasy", 20, 15)

    return new_book.add()

@book_searchbp.route("/")
def search():
    return BookManager.book_search("Python")
