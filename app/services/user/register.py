# To-Do: Test add function

from app import db
from app.models.user import Users
from app.utils.response import Response

def add(user_data) :

    existing_user = Users.query.filter_by(email=user_data.email).first()

    if existing_user:
        return Response.fail("Invalid email or password.", 401)
    
    user = Users(
        name=user_data.name,
        email=user_data.email
    )

    user.password = user_data.password

    db.session.add(user)
    db.session.commit()

    return Response.success(user)