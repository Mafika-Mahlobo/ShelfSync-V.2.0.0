from flask import Blueprint, request, render_template, jsonify
from app.models.user import User
from app.services.user_service import UserManager

user_routesbp = Blueprint("user", __name__, url_prefix="/users")

@user_routesbp.route("/add", methods=["POST"])
def add_users():
     if request.is_json:
          data = request.get_json()
     else:
          data = request.form.to_dict()
          
     user = User(**data)
     response = UserManager.save_to_db(user)
     return response["message"]


@user_routesbp.route("/delete/<id>", methods=["DELETE"])
def delete_user(id):
     response = UserManager.delete_user(id)
     return response["message"]

@user_routesbp.route("/list", methods=["GET"])
def list_users():
     response = UserManager.list_users()
     if response["success"]:
          return response["data"]
     return response["message"]       

@user_routesbp.route("/get-users/<role>/<library_id>", methods=["GET"])
def get_users(role, library_id):
     response = UserManager.filter_users(role, library_id)
     if response["data"] == []:
          return response["message"]
     return response["data"]

@user_routesbp.route("/get-user/<id>", methods=["GET"])
def get_user(id):
     response = UserManager.get_user(id)
     if response["data"] == []:
          return response["message"]
     return response["data"]


@user_routesbp.route("/update/<id>", methods=["PUT"])
def edit_user(id):
     if request.is_json:
          data = request.get_json()
     else:
          data = request.form.to_dict()

     new_user = User(**data)
     response = UserManager.update_user_info(new_user, id, new_user.library_id)
     return response["message"]


@user_routesbp.route("/search/<query>", methods=["GET"])
def user_search(query):
     response = UserManager.user_search(query)
     if response["data"] == []:
          return response["message"]
     return response["data"]