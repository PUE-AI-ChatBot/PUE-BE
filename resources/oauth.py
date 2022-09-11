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

class GoogleLogin(Resource):
    _user_parser = reqparse.RequestParser()
    _user_parser.add_argument('email',
                              type=str,
                              required=True,
                              help="Field named 'email' cannot be blank."
                              )
    _user_parser.add_argument('name',
                              type=str,
                              required=True,
                              help="Field named 'name' cannot be blank."
                              )
    _user_parser.add_argument('id',
                              type=str,
                              required=True,
                              help="Field named 'id' cannot be blank."
                              )

    def post(self):
        data = GoogleLogin._user_parser.parse_args()
        user = UserModel.find_oauth_by_id(data['id'],'google')

        if not user :
            user = UserModel.find_by_username(data['email'])
            if not user :
                user = UserModel(
                    user_subname=data['name'],
                    user_name=data['email'],
                    provider='google',
                    pid=data['id']
                )
                user.save_to_db()
            else :
                user.provider = 'google'
                user.pid = data['id']

        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)
        return {
                   'access_token': access_token,
                   'refresh_token': refresh_token,
                   'user_id': user.id
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


class KakaoLogin(Resource):
    _user_parser = reqparse.RequestParser()
    _user_parser.add_argument('email',
                              type=str,
                              required=True,
                              help="Field named 'email' cannot be blank."
                              )
    _user_parser.add_argument('nickname',
                              type=str,
                              required=True,
                              help="Field named 'name' cannot be blank."
                              )
    _user_parser.add_argument('id',
                              type=str,
                              required=True,
                              help="Field named 'id' cannot be blank."
                              )

    def post(self):
        data = KakaoLogin._user_parser.parse_args()
        user = UserModel.find_oauth_by_id(data['id'], 'kakao')

        if not user:
            user = UserModel.find_by_username(data['email'])
            if not user:
                user = UserModel(
                    user_subname=data['nickname'],
                    user_name=data['email'],
                    provider='kakao',
                    pid=data['id']
                )
                user.save_to_db()
            else :
                user.provider = 'kakao'
                user.pid = data['id']

        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)
        return {
                   'access_token': access_token,
                   'refresh_token': refresh_token,
                   'user_id': user.id
               }, 200
