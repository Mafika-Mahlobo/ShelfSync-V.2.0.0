from flask import Blueprint, request, render_template, jsonify
from app.models.library import Library

librarybp = Blueprint("library", __name__, url_prefix="/register-library")

@librarybp.route("/")
def add_book():
    new_library = Library("ALX library", "Our new test library", "https://mynewlib.com")
    return new_library.add()