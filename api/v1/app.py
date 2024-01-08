#!/usr/bin/python3
"""
The app
"""


from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
hoster = getenv('HBNB_API_HOST')
if not hoster:
    hoster = '0.0.0.0'

porter = getenv('HBNB_API_PORT')
if not porter:
    porter = 5000


@app.teardown_appcontext
def teardown(error):
    """Clean"""
    storage.close()


if __name__ == '__main__':
    app.run(host=hoster, port=porter, threaded=True)
