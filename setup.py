import os
import pymongo
from flask import Flask

def setup():
    app = Flask(__name__)
    app.config.from_object('settings')

    config = app.config
    conn = pymongo.connection.Connection(config['MONGODB_HOST'],
                                         config['MONGODB_PORT'])
    db = conn[config['MONGODB_DB']]

    return app, db

app, db = setup()
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

