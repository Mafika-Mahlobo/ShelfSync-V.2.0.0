from flask import Blueprint, request, render_template, jsonify
from app.models.library import Library
from app.services.library_service import LibraryManager

librarybp = Blueprint("library", __name__, url_prefix="/register-library")
library_deletebp = Blueprint("library_delete", __name__, url_prefix="/delete-library")
library_getbp = Blueprint("library_get", __name__, url_prefix="/get_libraries")
library_searchbp = Blueprint("search_library", __name__, url_prefix="/library_search")
library_editbp = Blueprint("edit_library", __name__, url_prefix="/edit_library")

@librarybp.route("/")
def add_library():
    new_library = Library("ALX library", "Our new test library", "https://mynewlib.com")
    response = LibraryManager.add_library(new_library)
    return response["message"]

@library_deletebp.route("/")
def delete_book():
    library = Library("Mafika's Library", "Another test library for update", "https://test.com")
    response = LibraryManager.delete_library(library)
    return response["message"]

@library_getbp.route("/")
def get_library():
    response = LibraryManager.get_libraries()
    return response["data"]

@library_searchbp.route("/")
def search_library():
    response = LibraryManager.search_by_name("AL")
    return response["data"]

@library_editbp.route("/")
def update_library():
    libraries = LibraryManager.get_libraries()
    library_id = libraries["data"][0][0]

    new_values = {"name": "Mafika's Library", 
                  "description": "Another test library for update", 
                  "logo_url": "https://test.com"}

    my_library = Library(**new_values)
    response = LibraryManager.edit_library(my_library, library_id)

    return response["message"]