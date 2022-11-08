from flask_socketio import Namespace, emit
from flask import session, request
from resources import main_ai
from models.user import UserModel
from models.chat import ChatModel
from models.statistic import StatisticModel
from datetime import datetime
from pytz import timezone
import eventlet


class ChatNamespace(Namespace):
    def on_connect(self):
        print("Client connected")
        self.user_id = 1
        main_ai.set_init()

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
        user.num_of_userchats += 1


        processed_data = main_ai.run("Chanee",data['message'])

        if processed_data["Emotion"]:
           stat= StatisticModel(
               user_id=user.id,
               date_YMD=now[:8]
           )
           stat.save_to_db()

        if processed_data["Flag"]:
            user.num_of_counselling += 1

        user.save_to_db()
        print(processed_data)
        eventlet.sleep(2)
        for content in processed_data["System_Corpus"] :
            now = datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S")
            emit("RECEIVE_MESSAGE", {"response": content,"day":now[:8],'time':now[8:]})
            chat = ChatModel(
                user_id=user.id,
                date_YMD=now[:8],
                date_YMDHMS=now,
                direction='BOT',
                utterance=content
            )
            chat.save_to_db()
            eventlet.sleep(3)

