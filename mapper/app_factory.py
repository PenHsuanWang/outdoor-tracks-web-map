import os

from flask import Flask, render_template
from flask.json import JSONEncoder
from flask_cors import CORS

from bson import json_util, ObjectId
from datetime import datetime, timedelta

from mapper.db import get_db
from mapper.api.map_object import Marker, marker_api_v1

class MongoJsonEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(APP_DIR, 'front_end/static')
    TEMPLATE_FOLDER = os.path.join(APP_DIR, 'front_end/templates')

    app = Flask(__name__, static_folder=STATIC_FOLDER,
                template_folder=TEMPLATE_FOLDER,)

    CORS(app)
    app.json_encoder = MongoJsonEncoder
    app.register_blueprint(marker_api_v1)

    @app.route('/')
    def root():
        return render_template('home/index.html')

    @app.route('/users/map/')
    def map():
        return render_template('map.html')

    @app.route('/users/profile/')
    def profile():
        return render_template('home/profile.html')

    @app.route('/login/')
    def login():
        return render_template('home/login.html')

    @app.route('/register/')
    def register():
        return render_template('home/register.html')

    # @app.route('/', defaults={'path': ''})
    # @app.route('/<path:path>')
    # def serve(path):
    #     return render_template('map.html')
    #
    @app.route('/test_db/')
    def test_db():
        with app.app_context():
            db = get_db()

            mountain_test = db.mountain_test
            print(mountain_test.find_one())

    @app.route('/save_marker/')
    def save_maker():
        with app.app_context():
            marker1 = Marker('24.5', '121.0', '123', 'maker1')
            marker1.save()

    return app

