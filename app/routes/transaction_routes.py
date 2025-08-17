from flask import Blueprint, request, render_template, jsonify
from app.models.transaction import Loans, Fines

check_outbp = Blueprint("loans_out", __name__, url_prefix="/check_out")
check_inbp = Blueprint("loan_in", __name__, url_prefix="check_in")

@check_outbp.route("/")
def check_out():
    transation = Loans(17, 5, 6, "08-17-2025 14:33:00", "08-25-2025 11:30:00", "08-22-2025 11:30:00", "Borrowed")
    return transation.check_out()
