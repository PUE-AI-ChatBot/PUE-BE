from models import StatisticModel
import json

def make_stats(user):

    stat = StatisticModel(
        date_YMD="20221102",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["걱정"] += 2
    temp["불만"] += 1
    temp["연민"] += 2
    temp["질투"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 6

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221101",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["중립"] += 3
    temp["기쁨"] += 2
    temp["죄책감"] += 4
    temp["당혹"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 10

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221031",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["중립"] += 2
    temp["기쁨"] += 3
    stat.emotions = json.dumps(temp)
    stat.total +=5

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221030",
        user_id=user.id
    )

    temp = json.loads(stat.emotions)
    temp["슬픔"] += 1
    temp["불만"] += 2
    temp["연민"] += 1
    stat.emotions = json.dumps(temp)
    stat.total +=4

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221029",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["기쁨"] += 1
    temp["당혹"] += 2
    temp["걱정"] += 3
    temp["질투"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 7

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221028",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["죄책감"] += 1
    temp["기쁨"] += 2
    temp["중립"] += 3
    temp["걱정"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 7

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221027",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["슬픔"] += 3
    temp["중립"] += 2
    temp["불만"] += 4
    temp["당혹"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 1

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221026",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["죄책감"] += 1
    temp["기쁨"] += 2
    temp["중립"] += 3
    temp["걱정"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 7

    stat.save_to_db()
