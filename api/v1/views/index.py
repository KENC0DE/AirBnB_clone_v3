#!/usr/bin/python3
"""A flask file with some defined routes"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def get_status():
    """ returns the status in json format"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def get_counts():
    """ Returns counts of all storage class"""
    from models.state import State
    from models import amenity
    from models import city
    from models import place
    from models import review
    from models import user

    classes = {
            'amenities': Amenity,
            'cities': City,
            'places': Place,
            'reviews': Review,
            'states': state,
            'users': User
            }
    counts = {}
    for key, value in in classes.items():
        counts.update({key: storage.count(value)})
    return jsonify(counts)
