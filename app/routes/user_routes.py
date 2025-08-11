from flask import Blueprint
from app.services.user_service import Patron

user_routesbp = Blueprint("user", __name__, url_prefix="/user")

@user_routesbp.route("/")
def show_users():
    mafika = Patron("Mafika Mahlobo")

    return mafika.create_user()