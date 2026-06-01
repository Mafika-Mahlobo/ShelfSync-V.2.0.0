from flask import request
from flask import Blueprint
from app.services.user.register import add
from app.utils.validators.register_validator import UserSchema
from app.utils.response import Response

users = Blueprint('users', __name__, url_prefix='/api/users')

@users.route('/', methods=['POST'])
def register_user():
    user = request.get_json()

    try:
        validated = UserSchema(**user)
    except ValueError as e:
        raise ValueError(Response.fail(e.errors(), 400))

    if validated:
        data = validated.model_dump()
        data.pop('confirm_password', None)
        response = add(**data)
        return response.to_http()
    
    return Response.fail('The was an issue processing you request.')