from models import StatisticModel
import json

def make_stats(user):

    stat = StatisticModel(
        date_YMD="20221108",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["걱정"] += 2
    temp["불만"] += 1
    temp["질투"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 4

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221107",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["중립"] += 3
    temp["기쁨"] += 2
    temp["당혹"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 6

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221106",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["중립"] += 2
    temp["기쁨"] += 3
    stat.emotions = json.dumps(temp)
    stat.total +=5

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221105",
        user_id=user.id
    )

    temp = json.loads(stat.emotions)
    temp["슬픔"] += 1
    temp["불만"] += 2
    stat.emotions = json.dumps(temp)
    stat.total +=3

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221104",
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
        date_YMD="20221103",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["기쁨"] += 2
    temp["중립"] += 3
    temp["걱정"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 6

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221102",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["슬픔"] += 3
    temp["중립"] += 2
    temp["불만"] += 4
    temp["당혹"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 10

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221101",
        user_id=user.id
    )
    temp = json.loads(stat.emotions)
    temp["기쁨"] += 2
    temp["중립"] += 3
    temp["걱정"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 6

    stat.save_to_db()
