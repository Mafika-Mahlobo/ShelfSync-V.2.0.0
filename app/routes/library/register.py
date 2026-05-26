from flask import request
from flask import Blueprint
from app.services.library.register import add
from app.utils.validators.register_validator import LibrarySchema
from app.utils.response import Response

libraries = Blueprint('library', __name__, url_prefix='/api/library')

@libraries.route('/', methods=['POST'])
def register_library():

    library = request.get_json()

    try:
        validated = LibrarySchema(**library)

    except ValueError as e:
        return Response.fail(e.errors(), 400)
    
    if validated:

        response = add(**validated.model_dump())
        return response.to_http()
    
    return Response.fail('There was an issue while processing your request.')