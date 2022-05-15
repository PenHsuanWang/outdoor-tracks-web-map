import bson
from flask import current_app, g
import pymongo
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy

# Configuration should be added from main entry,
# but have no idea about correct way to passing information by app factory method
# Using in this way temporary
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

MONGO_ATLAS_URL = config['PROD']['DB_URI']
#
#
# def get_db():
#     """
#     Configuration method to return db instance
#     :return:
#     """
#
#     if 'db' not in g:
#         client = connect_to_mongo_db(MONGO_ATLAS_URL)
#
#         try:
#             print(client.server_info())
#         except Exception:
#             print("Unable to connect to the server.")
#
#         g.db = client.test
#         db = LocalProxy(g.db)
#
#     return db
#
#
# def connect_to_mongo_db(mongo_uri: str):
#
#     client = pymongo.MongoClient(
#         mongo_uri,
#         serverSelectionTimeoutMS=5000
#     )
#
#     return client

def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = PyMongo(current_app, uri=MONGO_ATLAS_URL).db

    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def add_marker(lat, lon, elev, note):
    """
    Adding one marker into the makrs collection, with the following fields:

    - "lat"
    - "lon"
    - "elev"
    - "note"

    """

    marker_doc = {'lat': lat, 'lon': lon, 'elev': elev, 'note': note}
    return db.makers.insert_one(marker_doc)