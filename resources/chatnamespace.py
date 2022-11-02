from flask_socketio import Namespace, emit
from flask import session, request
from resources import main_ai
from models.user import UserModel
from models.chat import ChatModel
from models.statistic import StatisticModel
from datetime import datetime
from pytz import timezone
import time,json
import eventlet

class ChatNamespace(Namespace):
    def on_connect(self):
        print("Client connected")
        self.user_id = 1

    def on_disconnect(self):
        print("Client disconnected")
        #sessioned = session.get()

    def on_SEND_MESSAGE(self,data):
        print(data)
        now = datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S")
        print("DAY: ",now[:8])
        print("TIME: ",now[8:])

        chat = ChatModel(
            user_id=self.user_id,
            date_YMD=now[:8],
            date_YMDHMS=now,
            direction='USER',
            utterance=data['message']
        )
        chat.save_to_db()

        user = UserModel.find_by_id(self.user_id)


        now = datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S")
        emit("RECEIVE_MESSAGE", {"response": processed_data["System_Corpus"],"day":now[:8],'time':now[8:]})

        chat = ChatModel(
            user_id=user.id,
            date_YMD=now[:8],
            date_YMDHMS=now,
            direction='BOT',
            utterance=processed_data["System_Corpus"]
        )
        chat.save_to_db()