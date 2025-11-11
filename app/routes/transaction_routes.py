from flask import Blueprint, request, render_template, jsonify
from app.models.transaction import Loans, Fines
from app.services.transaction_service import TransactionManager
from app.services.user_service import UserManager
import datetime

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

@transactionsbp.route("/checkin/<loan_id>", methods=["POST"])
def check_in(loan_id):

    response = TransactionManager.check_in(loan_id)
    return response["message"]

@transactionsbp.route("/list/<user_id>", methods=["GET"])
def filter_loans(user_id):

    response = TransactionManager.filter_loans(user_id)

    if response["success"]:
        return response["data"]
    else:
        return response["message"]
    
@transactionsbp.route("/all_loans", methods=["GET"])
def list_all_loans():

    response = TransactionManager.list_all_loans()

    if response["success"]:
        return response["data"]
    else:
        return response["message"]
    

@transactionsbp.route("/fines/<user_id>", methods=["GET"])
def list_fines(user_id):
    response = TransactionManager.list_fines(user_id)

    if response["success"]:
        return response["data"]
    else:
        return response["message"]
    
@transactionsbp.route("/issue_fines", methods=["POST"])
def issue_fine():
        
        users = UserManager.list_users()["data"]

        for user in users:
            loans = filter_loans(user[0])
            print(loans)
            if isinstance(loans, str):
                print(loans)
            else:
                for loan in loans:
                    print(loan["due_date"])
                    if loan['due_date'] <= datetime.datetime.now():
                        TransactionManager.issue_fine(loan["id"])
                    pass

        return "Fines issued to overdue loans."