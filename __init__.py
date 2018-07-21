import os
from flask import Flask
from sqlalchemy import create_engine, asc, exc
from sqlalchemy.orm import sessionmaker
import json

from .models import Base

def create_app(test_config=None):
    # create and configure the create
    app = Flask(__name__, instance_relative_config=True)
    APPLICATION_NAME = "Dream Machine"
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'dreams.sqlite')
    )
    CLIENT_ID = json.loads(
        open('Dream_Machine/client_secrets.json',
             'r').read())['web']['client_id']

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #configure the database
    engine = create_engine('sqlite:///dream_db.db',
                           connect_args={'check_same_thread': False})
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # a simple page that says Hello
    @app.route('/hello')
    def hello():
        return 'Hello World'

    return app
