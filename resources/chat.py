from flask_restful import Resource, reqparse
from models.chat import ChatModel
from flask_jwt_extended import jwt_required, get_jwt_identity

class NumberChatList(Resource):
    def get(self,date, number):
        user_id = 1
        chats = [chat.json() for chat in ChatModel.find_by_number_with_user_id(user_id,date,number)]
        return {'chats': chats}, 200

class RangeChatList(Resource):
    def get(self,end,begin):
        user_id = 1
        chats = [chat.json() for chat in ChatModel.find_range_with_user_id(user_id, begin,end)]

        return {'chats': chats}, 200

class YMDChatList(Resource):
    def get(self,day):
        user_id = 1
        chats = [chat.json() for chat in ChatModel.find_all_by_dateYMD_with_user_id(user_id,day)]

        return {'chats': chats},200

class AllChatList(Resource):
    def get(self):
        user_id = 1
        chats = [chat.json() for chat in ChatModel.find_all_by_user_id(user_id)]

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

    def post(self,date):
        user_id = 1

        data = OneChat.parser.parse_args()

        chat = ChatModel(user_id,date[:8],data['direction'],data['utterance'])

        try:
            chat.save_to_db()
        except Exception as e:
            return {"message": "An error occurred creating the chat."}, 500

        return chat.json(), 201


    def delete(self, date):
        user_id = 1
        chat = ChatModel.find_by_fulldate_with_user_id(user_id,date)
        if chat:
            chat.delete_from_db()

        return {'message': 'Chat deleted'}, 200