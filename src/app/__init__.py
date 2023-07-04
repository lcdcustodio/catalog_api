from flask import Flask, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

#db = SQLAlchemy()
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('./src/app/credentials.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


def create_app(env=None):
    from app.routes import register_routes

    app = Flask(__name__)

    api = Api(app, title='Catalog API', version="1.0",description='Recomendações')
    """
    if env == 'test':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_test.db'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    """


    register_routes(api,app)
    """
    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")    
    """    

    return app