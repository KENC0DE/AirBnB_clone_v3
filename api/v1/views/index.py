#!/usr/bin/python3
"""A flask file with some defined routes"""
from flask import Flask, jsonify
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/status')
def get_status():
    """ returns the status in json format"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def get_counts():
    """ Returns counts of all storage class"""
    counts = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'reviews': storage.count('Review'),
            'states': storage.count('state'),
            'users': storage.count('User')
            }
    return jsonify(counts)
