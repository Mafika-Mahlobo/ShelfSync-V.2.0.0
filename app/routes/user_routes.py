from flask import Blueprint, request, render_template, jsonify
from app.models.user import User

user_routesbp = Blueprint("user", __name__, url_prefix="/register-user")

@user_routesbp.route("/")
def add_users():
    mock_form_data = {
        "library_id": 1,
        "name": "Mafika", ""
        "surname": "Mahlobo", 
        "email": "test@email.com", 
        "phone": "06754833", 
        "password": "123", 
        "role": 1,
        }
    new_user = User(
        mock_form_data["library_id"],
        mock_form_data["name"],
        mock_form_data["surname"],
        mock_form_data["email"], 
        mock_form_data["phone"], 
        mock_form_data["password"],
        mock_form_data["role"],
        )
    return User.add(new_user)