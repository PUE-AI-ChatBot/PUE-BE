from flask_restful import Resource, reqparse, request
from flask import redirect
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
import requests
from urllib.parse import urlencode
from configure import app
from models.user import UserModel

class GoogleOauth(Resource):
    def get(self):
        authorize_endpoint = app.config.get('GOOGLE_OAUTH_ENDPOINT')
        client_id = app.config.get('GOOGLE_CLIENT_ID')
        redirect_uri = app.config.get('GOOGLE_REDIRECT_URI')
        response_type = "code"
        scope = app.config.get("GOOGLE_SCOPES")

        query_string = urlencode(dict(
            redirect_uri=redirect_uri,
            client_id=client_id,
            scope=scope,
            response_type=response_type
        ))

        authorize_redirect = f'{authorize_endpoint}?{query_string}'
        return redirect(authorize_redirect)

class GoogleCallback(Resource):
    def get(self):

        code = request.args.get('code')
        token_endpoint = app.config.get('GOOGLE_TOKEN_ENDPOINT')
        client_id = app.config.get('GOOGLE_CLIENT_ID')
        client_secret = app.config.get('GOOGLE_CLIENT_KEY')
        redirect_uri = app.config.get('GOOGLE_REDIRECT_URI')
        grant_type = 'authorization_code'

        res = requests.post(token_endpoint, data=dict(
            code=code,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            grant_type=grant_type
        )).json()

        token_response = requests.get(
            app.config['GOOGLE_AUTH_URL'],
            headers={"Authorization":"Bearer " + res['access_token']},
        )

        if token_response.status_code != 200 :
            return {'message': "Cannot login with google..."},400

        data = token_response.json()
        user = UserModel.find_by_username(data['email'])
        if user :
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                       'access_token': access_token,
                       'refresh_token': refresh_token,
                       'user_id': user.id,
                   }, 200
        else :
            user = UserModel(user_name=data['email'],user_subname=data['name'],provider="google",pid=data['id'])
            user.save_to_db()

            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                       'access_token': access_token,
                       'refresh_token': refresh_token,
                       'user_id': user.id,
                        'message':"New user has registered!"
                   }, 200

class KakaoOauth(Resource):

    def get(self):
        authorize_endpoint = app.config.get('KAKAO_OAUTH_ENDPOINT')
        client_id = app.config.get('KAKAO_CLIENT_ID')
        redirect_uri = app.config.get('KAKAO_REDIRECT_URI')
        response_type = "code"
        scope = app.config.get("KAKAO_SCOPES")

        query_string = urlencode(dict(
            redirect_uri=redirect_uri,
            client_id=client_id,
            response_type=response_type,
            scope=scope
        ))

        authorize_redirect = f'{authorize_endpoint}?{query_string}'
        return redirect(authorize_redirect)


class KakaoCallback(Resource):
    def get(self):

        code = request.args.get('code')
        token_endpoint = app.config.get('KAKAO_TOKEN_ENDPOINT')
        client_id = app.config.get('KAKAO_CLIENT_ID')
        client_secret = app.config.get('KAKAO_CLIENT_KEY')
        redirect_uri = app.config.get('KAKAO_REDIRECT_URI')
        grant_type = 'authorization_code'

        res = requests.post(token_endpoint, data=dict(
            code=code,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            grant_type=grant_type
        )).json()

        token_response = requests.get(
            app.config['KAKAO_AUTH_URL'],
            headers={"Authorization": "Bearer " + res['access_token']},
        )
        if token_response.status_code != 200:
            return {'message': "Cannot login with kakao..."}, 400

        data = token_response.json()
        user = UserModel.find_by_username(data['kakao_account']['email'])
        if user:
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                       'access_token': access_token,
                       'refresh_token': refresh_token,
                       'user_id': user.id,
                   }, 200
        else:
            user = UserModel(user_name=data['kakao_account']['email'], user_subname=data['kakao_account']['profile']['nickname'], provider="kakao", pid=data['id'])
            user.save_to_db()

            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                       'access_token': access_token,
                       'refresh_token': refresh_token,
                       'user_id': user.id,
                       'message': "New user has registered!"
                   }, 200
