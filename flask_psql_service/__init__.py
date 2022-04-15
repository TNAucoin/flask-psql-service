__version__ = '0.1.0'

# third-party imports
import json
from flask import Flask
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
        from .models import Result
        result = Result('www.test.com',json.dumps({"a":1}),json.dumps({"b":2}))
        db.session.add(result)
        db.session.commit()
        return 'Hello, World!'
    
    migrate = Migrate(app, db)

    from flask_psql_service import models

    return app
