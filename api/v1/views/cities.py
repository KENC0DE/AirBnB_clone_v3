#!/usr/bin/python3
"""Handles all city default RESTFul API actions"""
from models.city import City
from models.state import State
from models import storage
from api.v1.views import app_views
from flask import request, make_response, abort, jsonify
from flasgger.utils import swag_from as swag


@app_views.route(
        '/states/<state_id>/cities', methods=['GET'], strict_slashes=False
        )
@swag('documentaion/city/cities_by_state.yml', method=['GET'])
def get_cities(state_id):
    """Lists all city objects of a specific state or city"""
    cities_ = []
    state = storage.get(State, state_id)
    if state:
        for city in state.cities:
            cities_.append(city.to_dict())
        return jsonify(cities_)
    abort(404)


@app_views.route('/cities/<city_id>/', methods=['GET'], strict_slashes=False)
@swag('documentation/city/get_city.yml', methods=['GET'])
def get_city(city_id):
    """ Retrieves city via id"""
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    abort(404)


@app_views.route(
        '/cities/<city_id>/', methods=['DELETE'], strict_slashes=False
        )
@swag('documentation/city/delete_city.yml', methods=['DELETE'])
def delete_city(city_id):
    """Deletes a city, based on the provided city id"""
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


@app_views.route(
        '/states/<state_id>/cities', methods=['POST'], strict_slashes=False
        )
@swag('documentaion/city/post_city.yml', method=['POST'])
def post_city(state_id):
    """ Creates City """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(404, description='Not a JSON')
    if 'name' not in request.get_json():
        abort(400, description='Missing name')
    resp = request.get_json()
    obj = City(**resp)
    obj.state_id = state.id
    obj.save()
    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/cities/<city_id>/', methods=['PUT'], strict_slashes=False)
@swag('documentation/city/delete_city.yml', methods=['PUT'])
def put_city(city_id):
    """ Updates a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if not request.get_json():
        abort(404, description='Not a JSON')
    lst = ['id', 'state_id', 'created_at', 'updated_at']
    obj = request.get_json()
    for key, value in obj.items():
        if key not in lst:
            setattr(city, key, value)
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
