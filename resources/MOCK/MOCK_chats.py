from models import ChatModel

def make_chats(user):
    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191522",
        direction="BOT",
        utterance="안녕하세요? Chanee님! 오늘 하루는 어떠셨나요?"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191528",
        direction="USER",
        utterance="내일 면접때문에 너무 걱정되서 아무것도 못했어..."
    )
    chat.save_to_db()


    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191534",
        direction="BOT",
        utterance="Chanee님이 느끼시는 감정의 이유에 대하여 좀 더 자세한 설명이 가능할까요?"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191545",
        direction="USER",
        utterance="영어로 면접 본다는데 난 영어 잘 못하거든..."
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191550",
        direction="BOT",
        utterance="그렇군요..적당한 걱정은 도움이 되지만 지나친 불안은 문제 해결을 방해하죠."
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191555",
        direction="BOT",
        utterance="Chanee님께서는 '영어로 면접 본다는데 난 영어 잘 못하거든...' 이라고 말씀하셨고 정말 걱정이 될만한 이유라고 생각이 들어요."
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191601",
        direction="BOT",
        utterance="제가 Chanee님에게 도움이 되길 원해요!"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191606",
        direction="BOT",
        utterance="다음 중에서 골라주실래요?"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191612",
        direction="BOT",
        utterance="| 책 추천 | 노래 추천 | 대화하기 | 상담사 연결 |"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191618",
        direction="USER",
        utterance="대화하기"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191623",
        direction="BOT",
        utterance="Chanee님의 말씀해주신 그런 고민들은 정말이지 누구에게나 머리 아프게 만들죠"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191628",
        direction="BOT",
        utterance="그래서 더욱 제대로 된 판단이 필요해요. 생각하시는 해결 방법을 적고 생각을 정리해보는 시간을 가져봐요!"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191630",
        direction="BOT",
        utterance="(자신이 생각하는 해결 방법을 적어주세요)"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191642",
        direction="USER",
        utterance="음, 한번 영어 스터디 그룹원들에게 피드백을 받아볼게!"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191648",
        direction="BOT",
        utterance="좋아요, 그럼 그 방법의 장단점은요?"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191655",
        direction="USER",
        utterance="그분들이랑 좀 어색하긴 한데... 아마 그분들한테도 도움이 될것같아"
    )
    chat.save_to_db()


    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191705",
        direction="BOT",
        utterance="좋아요! 지금 세워본 방법이 실제로 도움이 되지 않더라도 이렇게 정리하는 것 만으로도 문제를 이해하고 해결하는데 큰 도움이 되죠!!"
    )
    chat.save_to_db()

    chat = ChatModel(
        user_id=user.id,
        date_YMD="20221102",
        date_YMDHMS="20221102191711",
        direction="BOT",
        utterance="마지막으로 이 말을 전해요! 사라져라 지겨운 걱정들아..!! -빨간 머리 앤-"
    )
    chat.save_to_db()