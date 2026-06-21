from flask_jwt_extended import create_access_token
from app.models.user import Users
from datetime import timedelta
from app.utils.response import Response

def login(email, password):

    user = Users.query.filter_by(email=email).first()

    if user:

        if user.check_password(password):

            token = create_access_token(
                    identity=user.id,
                    expires_delta= timedelta(minutes=15)
                )
            
            return Response.success({'token': token}, 200)
        
        return Response.fail('Invalid username or password.', 401)
    
    return Response.fail('Invalid username and password', 401)