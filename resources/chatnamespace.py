from flask_socketio import Namespace, emit
from flask import session, request
from resources import main_ai
from models.user import UserModel
from models.chat import ChatModel
from datetime import datetime
from pytz import timezone
from .MOCK import mocks
import time,json

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

        if user.cursor :
            if self.scenario_processor(user,data['message']) :
                user.value_container = json.dumps({'name':user.user_subname})
        else :
            processed_data = main_ai.run("Hello", data['message'])
            if processed_data["Emotion"] in ['걱정']:
                user.cursor = '1'
                user.save_to_db()

                self.scenario_processor(user,data['message'])
            else :
                now = datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S")
                self.emit("RECEIVE_MESSAGE", {"response": processed_data["System_Corpus"],"day":now[:8],'time':now[8:]})
                chat = ChatModel(
                    user_id=user.id,
                    date_YMD=now[:8],
                    date_YMDHMS=now,
                    direction='BOT',
                    utterance=processed_data["System_Corpus"]
                )
                chat.save_to_db()

    def scenario_processor(self,user, res):
        data = mocks[user.cursor]
        setups = data['setup']

        value_container = json.loads(user.value_container)

        if user.res_controller:
            value_container[user.res_controller] = res

        for text, keys in zip(data['text'], setups['keys']):
            time.sleep(setups['timer'])
            now = datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S")
            real_keys = [value_container[key] if (key in value_container.keys()) else key for key in keys]

            self.emit("RECEIVE_MESSAGE", {"response": text.format(*real_keys), "day": now[:8], 'time': now[8:]})

            chat = ChatModel(
                user_id=user.id,
                date_YMD=now[:8],
                date_YMDHMS=now,
                direction='BOT',
                utterance=text.format(*real_keys)
            )
            chat.save_to_db()

        if setups['is_response']:
            res_setup = data['response']
            if res_setup["is_store"]:
                user.res_controller = res_setup['store_key']
            else:
                user.res_controller = None
        else:
            user.res_controller = None

        user.cursor = setups['next']
        user.value_container = json.dumps(value_container)
        user.save_to_db()

        if setups["is_last"]:
            return False

        return True