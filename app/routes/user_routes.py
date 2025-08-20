from flask import Blueprint, request, render_template, jsonify
from app.models.user import User
from app.services.user_service import UserManager
from app.services.library_service import LibraryManager
from app.config import User_role

user_routesbp = Blueprint("user", __name__, url_prefix="/register-user")
user_deletebp = Blueprint("user_delete", __name__, url_prefix="/delete-user")
user_getbp = Blueprint("get_users", __name__, url_prefix="/get_users")
user_editbp = Blueprint("edit_user", __name__, url_prefix="/edit_user")

@user_routesbp.route("/")
def add_users():
    mock_form_data = {
        "library_id": 14,
        "name": "Mafika",
        "surname": "Mahlobo", 
        "email": "test@email.com", 
        "phone": "06754833", 
        "password": "123", 
        "role": 0,
        }
    
    user = User(**mock_form_data)
    response = UserManager.save_to_db(user)
    return response["message"]

@user_deletebp.route("/")
def delete_user():
     mock_form_data = {
        "library_id": 14,
        "name": "Lucia",
        "surname": "Mbushi", 
        "email": "Lucia@email.com", 
        "phone": "1234382", 
        "password": "123", 
        "role": 1,
        }
     
     user = User(**mock_form_data)
     response = UserManager.delete_user(user)
     return response["message"]

@user_getbp.route("/")
def get_users():
     library_id = LibraryManager.get_libraries()["data"][0][0]
     user_type = User_role["Patron"]
     response = UserManager.get_users(user_type, library_id)
     return response["data"]

@user_editbp.route("/")
def edit_user():
     user_type = User_role["Patron"]
     library_id = LibraryManager.get_libraries()["data"][0][0]
     user_id = UserManager.get_users(user_type, library_id)["data"][0][0]
     mock_data = {
          "library_id": library_id,
          "name": "Lucia",
          "surname": "Mbushi",
          "email": "Lucia@email.com",
          "phone": "1234382",
          "password": "123@44",
          "role": user_type
     }

     new_user = User(**mock_data)
     response = UserManager.update_user_info(new_user, user_id, library_id)
     return response["message"]
