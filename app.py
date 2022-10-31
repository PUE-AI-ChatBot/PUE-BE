from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from models import *
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from resources import create_api, create_socketio
from configure import app
from db import db

host = "0.0.0.0"
port = 5000

app.secret_key = "chan"
db_name = "pue"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SERVER_HOST'] = "localhost:3000"

#GOOGLE_OAUTH
app.config['GOOGLE_CLIENT_ID'] = "14896673180-u6cbabk7l3dt6gcrlb6egnch25s2l90h.apps.googleusercontent.com"
app.config['GOOGLE_CLIENT_KEY'] = "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"
app.config['GOOGLE_OAUTH_ENDPOINT'] = "https://accounts.google.com/o/oauth2/auth"
app.config['GOOGLE_TOKEN_ENDPOINT']="https://oauth2.googleapis.com/token"
app.config['GOOGLE_REDIRECT_URI'] = f"http://{app.config['SERVER_HOST']}/oauth/callback/google"
#app.config['GOOGLE_REDIRECT_URI'] = f"http://localhost:5001/login/google"
app.config['GOOGLE_AUTH_URL']= "https://www.googleapis.com/userinfo/v2/me"
app.config['GOOGLE_SCOPES'] = "email profile"

#KAKAO_OAUTH
app.config['KAKAO_CLIENT_ID'] = "f0af74e24a928840538f00331e5d3317"
app.config['KAKAO_CLIENT_KEY'] = "IlswqcO2pIMCguIROJ67suFTkhBi8bOg"
app.config['KAKAO_OAUTH_ENDPOINT'] = "https://kauth.kakao.com/oauth/authorize"
app.config['KAKAO_TOKEN_ENDPOINT']="https://kauth.kakao.com/oauth/token"
app.config['KAKAO_REDIRECT_URI'] = f"http://{app.config['SERVER_HOST']}/oauth/callback/kakao"
#app.config['KAKAO_REDIRECT_URI'] = f"http://localhost:5001/login/kakao"
app.config['KAKAO_AUTH_URL']= "https://kapi.kakao.com/v2/user/me"
app.config['KAKAO_SCOPES'] = "account_email profile_nickname"

#SECRET_KEY = config['DEFAULT']['SECRET_KEY']
#db_name = config['DEFAULT']['DB_NAME']+'.db'

#SETUP
#1. virtualenv venv --python=python3.8
#2. Flask-RESTful
#3. Flask-JWT

api = Api(app) #API FLASK SERVER
#CORS(app)

sock = SocketIO(app,cors_allowed_origins="*")

#this will be used for login(authenticate users)
jwt = JWTManager(app) #this will make endpoint named '/auth' (username,password)
#JWT will be made based on what authenticate returns(user) and JWT will be sent to identity to identify which user has Vaild JWT
bcrypt = Bcrypt(app)

create_api(api)
create_socketio(sock)

@jwt.invalid_token_loader
def invalid_token_callback(error):  # we have to keep the argument here, since it's passed in by the caller internally
    return jsonify({
        'message': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "description": "Request does not contain an access token.",
        'error': 'authorization_required'
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        "description": "The token has been revoked.",
        'error': 'token_revoked'
    }), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "description": "Request does not contain an access token.",
        'error': 'authorization_required'
    }), 401


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":

    db.init_app(app)
    print("Now we Run...")
    #app.run(port=5000,debug=False) #debug tells us what is problem

    sock.run(app,host=host,port=port,debug=False)