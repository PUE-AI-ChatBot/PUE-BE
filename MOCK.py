from models.user import UserModel
from models.chat import ChatModel
from models.statistic import StatisticModel
import json

def make_dummy():
    user = UserModel(
        user_name="well87865@gmail.com",
        user_subname="Chanee",
        password="123123"
    )
    user.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20220906",
        date_YMDHMS="20220906151522",
        direction="USER",
        utterance="안녕하세요!"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20220906",
        date_YMDHMS="20220906151540",
        direction="BOT",
        utterance="네! 안녕하세요!"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20220908",
        date_YMDHMS="20220908020022",
        direction="USER",
        utterance="나 우울해..."
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20220908",
        date_YMDHMS="20220908020030",
        direction="BOT",
        utterance="무슨 일이 있으신가요??"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20220910",
        date_YMDHMS="20220910235640",
        direction="USER",
        utterance="내일 봐!"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20220910",
        date_YMDHMS="20220910235645",
        direction="BOT",
        utterance="네, 좋은 밤 되세요."
    )
    chat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220906",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["중립"]+=1
    stat.emotions = json.dumps(temp)
    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220908",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["슬픔"] += 1
    stat.emotions = json.dumps(temp)
    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220910",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["기쁨"] += 1
    stat.emotions = json.dumps(temp)
    stat.save_to_db()