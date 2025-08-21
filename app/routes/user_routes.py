from flask import Blueprint, request, render_template, jsonify
from app.models.user import User
from app.services.user_service import UserManager

user_routesbp = Blueprint("user", __name__, url_prefix="/register-user")
user_deletebp = Blueprint("user_delete", __name__, url_prefix="/delete-user")
user_getbp = Blueprint("get_users", __name__, url_prefix="/get_users")
user_editbp = Blueprint("edit_user", __name__, url_prefix="/edit_user")
user_edit_profilebp = Blueprint("edit_profile", __name__, url_prefix="/edit_profile")
user_searchbp = Blueprint("user_search",  __name__, url_prefix="/user_search")

@user_routesbp.route("/")
def add_users():
     if request.is_json:
          data = request.get_json()
     else:
          data = request.form.to_dict()
          
     user = User(**data)
     response = UserManager.save_to_db(user)
     return response["message"]


@user_deletebp.route("/")
def delete_user():
     if request.is_json:
          data = request.get_json()
     else:
          data = request.form.to_dict()
     
     user = User(**data)
     response = UserManager.delete_user(user)
     return response["message"]

@user_getbp.route("/")
def get_users():
     if request.is_json:
          query = request.get_json()
     else:
          query = request.form.to_dict()

     response = UserManager.get_users(query["user_type"], query["library_id"])
     return response["data"]

@user_editbp.route("/")
def edit_user():
     if request.is_json:
          data = request.get_json()
     else:
          data = request.form.to_dict()

     new_user = User(**data)
     response = UserManager.update_user_info(new_user, new_user.user_id, new_user.library_id)
     return response["message"]

@user_edit_profilebp.route("/")
def edit_profile():
     if request.is_json:
          data = request.get_json()
     else:
          data = request.form.to_dict()

     user = User(**data)
     response = UserManager.edit_user_profile(user)
     return response["message"]

@user_searchbp.route("/")
def user_search():
     if request.is_json:
          search_strings = request.get_json()
     else:
          search_strings = request.form.to_dict()

     response = UserManager.user_search(search_strings["query"], search_strings["is_admin"])
     return response["data"]