from flask import Blueprint, request, render_template, jsonify
from app.models.transaction import Loans, Fines
from app.services.transaction_service import TransactionManager

transactionsbp = Blueprint("transactions", __name__, url_prefix="/transactions")


@transactionsbp.route("/checkout/<resource_id>", methods=["POST"])
def check_out(resource_id):
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    loan_information = Loans(**data)
    response = TransactionManager.check_out(resource_id, loan_information)
    return response["message"]
