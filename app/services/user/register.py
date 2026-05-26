# To-Do: Test add function

from app import db
from app.models.user import Users
from app.utils.response import Response

def add(user_obj):

    existing_user = Users.query.filter_by(email=user_obj['email']).first()

    if existing_user:
        return Response.fail("Invalid email or password.", 401)
    
    user = Users(
        name=user_obj['name'],
        email=user_obj['email']
    )

    user.password = user_obj['password']

    db.session.add(user)
    db.session.commit()

    return Response.success(user.to_dict(), 201)