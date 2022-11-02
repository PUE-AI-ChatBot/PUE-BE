from db import db
from . import and_
import json

init_emotion={
    "불만":0, "중립":0, "당혹":0, "기쁨":0, "걱정":0, "질투":0, "슬픔":0, "죄책감":0, "연민":0
}

class StatisticModel(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    date_YMD = db.Column(db.String(80))
    emotions = db.Column(db.String(80))
    total = db.Column(db.Integer())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, date_YMD,user_id):
        self.date_YMD = date_YMD
        self.emotions = json.dumps(init_emotion.copy())
        self.total = 0
        self.user_id = user_id

    def json(self):
        emotions = json.loads(self.emotions)
        return {
            'date':self.date_YMD,
            'top_emotion': max(emotions,key=emotions.get),
            'chart':{
                'total': self.total,
                'emotions': emotions
            }
        }

    #1. day인 경우, month를 받으면 해당월에 관련된 모든 day 통계 표출
    #2. day인 경우, start와 end를 받으면 해당 기간에 관련된 모든 day 통계 표출
    #3. week인 경우, month를 받으면 해당 월과 관련된 모든 week 통계 표출
    #4. week인 경우, start를 받으면 해당 기간에 관련된 week 표출
    #5. month인 경우, month를 받으면 해당 월과 관련된 month 통계 표출

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).all()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    ##week, day는 시작 날짜, 양식은 YYYYMMDD
    ##month면 start_date 양식은 YYYYMM

    @classmethod
    def find_by_dateYMD_with_user_id(cls, user_id, date):
        return cls.query.filter(and_(cls.user_id == user_id, cls.date_YMD == date)).first()

    @classmethod
    def find_range_with_user_id(cls, user_id, begin, latest):
        return cls.query.filter(and_(cls.date_YMD.between(begin, latest), cls.user_id == user_id)).all()

    @classmethod
    def find_by_number_with_user_id(cls, user_id, latest, number):
        return cls.query.filter(and_(cls.date_YMD < latest, cls.user_id == user_id)).order_by(cls.id.desc()).limit(
            number).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
