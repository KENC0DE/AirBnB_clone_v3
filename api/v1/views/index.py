#!/usr/bin/python3
"""A flask file with some defined routes"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """ returns the status in json format"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ Returns counts of all storage class"""
    from models.state import State
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.user import User
    from models.amenity import Amenity

    classes = {"amenities": Amenity, "cities": City,
               "places": Place, "reviews": Review,
               "states": State, "users": User}

    counts = {}
    for key, val in classes.items():
        counts.update({key: storage.count(val)})

    return jsonify(counts)
