from app.models.library import Libraries
from app.utils.response import Response
from app import db


def add(name, description, location_address, latitude, longitude):
    
    existing_library = Libraries.query.filter(
        Libraries.name == name,
        Libraries.location_address == location_address
    ).first()

    if existing_library:
        raise ValueError(Response.fail('Library already exists'))
    
    new_library = Libraries(
        name=name,
        description=description,
        location_address=location_address,
        latitude=latitude,
        longitude=longitude
    )

    db.session.add(new_library)
    db.session.commit()

    return Response.success(status_code=201)