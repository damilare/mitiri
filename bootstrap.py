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

from public.views import pages

app.register_blueprint(pages)

if __name__ == '__main__':
    app.run(debug=True)