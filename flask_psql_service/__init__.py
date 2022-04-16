__version__ = '0.1.0'

# third-party imports
import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/person/<id>', methods=['GET'])
    def get_person(id):
        # TODO: figure out a way around circular ref here
        from .models import Person
        person = Person.query.get(id)
        del person.__dict__['_sa_instance_state']
        return jsonify(person.__dict__)

    @app.route('/person/create', methods=['POST'])
    def create_person():
        # TODO: figure out a way around circular ref here
        from .models import Person
        body = request.get_json()
        person = Person(body['first_name'], body['last_name'], body['age'])
        db.session.add(person)
        db.session.commit()
        return 'person created'

    migrate = Migrate(app, db)
    from flask_psql_service import models

    return app
