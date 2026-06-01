# To-Do: Test add function

from app import db
from app.models.user import Users
from app.utils.response import Response

def add(name, email, password):

    existing_user = Users.query.filter_by(email=email).first()

    if existing_user:
        return Response.fail("Invalid email or password.", 401)
    
    user = Users(
        name=name,
        email=email
    )

    user.password = password

    db.session.add(user)
    db.session.commit()

    return Response.success(user.to_dict(), 201)