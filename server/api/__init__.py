#   IMPORTING LIBRARIES
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS   # TO GET RID OF THE CORS ERROR

db = SQLAlchemy()

#  DEFINING FUNCTIONS


def create_app():

    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'    #    DEFINING DATABASE

    db.init_app(app)  # APP IS INITIATED

    #   REGISTERING BLUEPRINT AFTER IMPORTING( NOT DONE AT THE TOP TO AVOID ERRORS)
    from .views import main
    app.register_blueprint(main)

    return app
