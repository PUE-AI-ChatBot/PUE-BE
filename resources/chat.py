from flask_restful import Resource, reqparse
from models.chat import ChatModel
from flask_jwt_extended import jwt_required, get_jwt_identity

class NumberChatList(Resource):
    @jwt_required()
    def get(self,date, number):
        user_id = get_jwt_identity()
        chats = [chat.json() for chat in ChatModel.find_by_number_with_user_id(user_id,date,number)]
        if not chats :
            return {"message":"None"},400

        return {'chats': chats}, 200

class RangeChatList(Resource):
    @jwt_required()
    def get(self,end,begin):
        user_id = get_jwt_identity()
        chats = [chat.json() for chat in ChatModel.find_range_with_user_id(user_id, begin,end)]

        if not chats :
            return {"message":"None"},400

        return {'chats': chats}, 200

class YMDChatList(Resource):
    @jwt_required()
    def get(self,day):
        user_id = get_jwt_identity()
        chats = [chat.json() for chat in ChatModel.find_all_by_dateYMD_with_user_id(user_id,day)]
        if not chats :
            return {"message":"None"},400

        return {'chats': chats},200

class AllChatList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        chats = [chat.json() for chat in ChatModel.find_all_by_user_id(user_id)]
        if not chats :
            return {"message":"None"},400

        return {'chats': chats},200

class OneChat(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('direction',
                        type=str,
                        required=True,
                        help="Field named 'direction' cannot be blank."
                        )
    parser.add_argument('utterance',
                        type=str,
                        required=True,
                        help="Field named 'utterance' cannot be blank."
                        )
    parser.add_argument('emotion',
                        type=str,
                        required=True,
                        help="Field named 'emotion' cannot be blank."
                        )

    @jwt_required()
    def post(self,date):
        user_id = get_jwt_identity()

        data = OneChat.parser.parse_args()

        chat = ChatModel(user_id,date[:8],data['direction'],data['utterance'])

        try:
            chat.save_to_db()
        except Exception as e:
            return {"message": "An error occurred creating the chat."}, 500

        return chat.json(), 201

    @jwt_required()
    def delete(self, date):
        user_id = get_jwt_identity()
        chat = ChatModel.find_by_fulldate_with_user_id(user_id,date)
        if chat:
            chat.delete_from_db()

        return {'message': 'Chat deleted'}, 200