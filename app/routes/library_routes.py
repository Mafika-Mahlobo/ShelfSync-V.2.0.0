from flask import Blueprint, request, render_template, jsonify
from app.models.library import Library

librarybp = Blueprint("library", __name__, url_prefix="/register-library")
library_deletebp = Blueprint("library_delete", __name__, url_prefix="/delete-library")

@librarybp.route("/")
def add_book():
    new_library = Library("ALX library", "Our new test library", "https://mynewlib.com")
    return new_library.add()

@library_deletebp.route("/")
def delete_book():
    library = Library("ALX library", "Our new test library", "https://mynewlib.com")
    return library.delete()