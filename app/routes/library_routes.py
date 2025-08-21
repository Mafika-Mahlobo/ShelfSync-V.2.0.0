from flask import Blueprint, request, render_template, jsonify
from app.models.library import Library
from app.services.library_service import LibraryManager
import json

librarybp = Blueprint("library", __name__, url_prefix="/register-library")
library_deletebp = Blueprint("library_delete", __name__, url_prefix="/delete-library")
library_getbp = Blueprint("library_get", __name__, url_prefix="/get_libraries")
library_searchbp = Blueprint("search_library", __name__, url_prefix="/library_search")
library_editbp = Blueprint("edit_library", __name__, url_prefix="/edit_library")

@librarybp.route("/")
def add_library():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    new_library = Library(**data)
    response = LibraryManager.add_library(new_library)
    return response["message"]

@library_deletebp.route("/")
def delete_library():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    library = Library(**data)
    response = LibraryManager.delete_library(library)
    return response["message"]

@library_getbp.route("/")
def get_library():
    response = LibraryManager.get_libraries()
    return response["data"]

@library_searchbp.route("/")
def search_library():
    query = request.get_json()
    response = LibraryManager.search_by_name(query)
    return response["data"]

@library_editbp.route("/")
def update_library():
    
    if request.is_json:
        new_values = request.get_json()
    else:
        new_values = request.form.to_dict()

    library_id = new_values["id"]
    my_library = Library(**new_values)
    response = LibraryManager.edit_library(my_library, library_id)

    return response["message"]