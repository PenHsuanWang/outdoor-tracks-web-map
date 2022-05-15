from mapper.db import get_db
from werkzeug.local import LocalProxy

from flask import Blueprint, request, jsonify
from mapper.db import add_marker

from flask_cors import CORS
from datetime import datetime

marker_api_v1 = Blueprint(
    'marker_api_v1', 'marker_api_v1', url_prefix='/marker')
CORS(marker_api_v1)


class Marker:

    def __init__(self, lat, lon, elev, note):
        self._lat = lat
        self._lon = lon
        self._elev = elev
        self._note = note

    @marker_api_v1.route('/saving')
    def save(self):
        print("Going to save marker")
        maker_doc = {
            'lat': self._lat,
            'lon': self._lon,
            'elev': self._elev,
            'note': self._note
        }
        add_marker(self._lat, self._lon, self._elev, self._note)
        print("Save Marker Successfully")

