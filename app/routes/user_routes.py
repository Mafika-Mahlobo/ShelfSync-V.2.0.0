from flask import Blueprint, request, render_template, jsonify
from app.models.user import User
from app.services.user_service import UserManager

user_routesbp = Blueprint("user", __name__, url_prefix="/register-user")
user_deletebp = Blueprint("user_delete", __name__, url_prefix="/delete-user")

@user_routesbp.route("/")
def add_users():
    mock_form_data = {
        "library_id": 11,
        "name": "Mafika",
        "surname": "Mahlobo", 
        "email": "test@email.com", 
        "phone": "06754833", 
        "password": "123", 
        "role": 1,
        }
    
    user = User(**mock_form_data)
    response = UserManager.save_to_db(user)
    return response["message"]

@user_deletebp.route("/")
def delete_user():
     mock_form_data = {
        "library_id": 11,
        "name": "Mafika",
        "surname": "Mahlobo", 
        "email": "test@email.com", 
        "phone": "06754833", 
        "password": "123", 
        "role": 1,
        }
     
     user = User(**mock_form_data)
     response = UserManager.delete_user(user)
     return response["message"]
          