from .MOCK import make_account, make_chats, make_stats
from flask_restful import Resource, reqparse, request

class MakeMock(Resource):
    def get(self):

        user = make_account()
        make_stats(user)
        #make_chats(user)

        return {"message":"OK"},200