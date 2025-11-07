from flask import Blueprint, request, render_template, jsonify
from app.models.library import Library, LibraryHours
from app.services.library_service import LibraryManager

librarybp = Blueprint("library", __name__, url_prefix="/library") 

@librarybp.route("/add", methods=["POST"])
def add_library():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    new_library = Library(**data)
    response = LibraryManager.add_library(new_library)
    return response["message"]


@librarybp.route("/delete/<id>", methods=["DELETE"])
def delete_library(id):

    response = LibraryManager.delete_library(int(id))
    return response["message"]

@librarybp.route("/<id>", methods=["GET"])
def get_library(id):
    response = LibraryManager.get_library(id)
    return response["data"]

@librarybp.route("/list", methods=["GET"])
def get_libraries():
    response = LibraryManager.get_libraries()
    return response["data"]

@librarybp.route("/search/<keyword>", methods=["GET"])
def search_library(keyword):
    response = LibraryManager.search_by_name(keyword)
    return response["data"]

@librarybp.route("/edit/<id>", methods=["PUT"])
def update_library(id):
    
    if request.is_json:
        new_values = request.get_json()
    else:
        new_values = request.form.to_dict()

    my_library = Library(**new_values)
    response = LibraryManager.edit_library(my_library, id)

    return response["message"]

@librarybp.route("/hours/add", methods=["POST"])
def library_hours():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    library = LibraryHours(**data)
    result = LibraryManager.set_library_hours(library)
    return result["message"]

@librarybp.route("/hours/edit/<library_id>", methods=["PUT"])
def library_hours_edit(library_id):
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    new_hours = LibraryHours(**data)

    response = LibraryManager.edit_library_hours(library_id, new_hours)
    return response["message"]

@librarybp.route("/hours/delete/<library_id>/<day_of_week>", methods=["DELETE"])
def library_hours_delete(library_id, day_of_week):
    response = LibraryManager.delete_hours(library_id, day_of_week)
    return response["message"]