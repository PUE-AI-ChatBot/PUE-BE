from db import db
from . import and_

class ChatModel(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    date_YMD = db.Column(db.String(80)) #YYYYMMDD
    date_YMDHMS = db.Column(db.String(80)) #YYYYMMDDHHMMSS
    direction = db.Column(db.String(80))#0-sender(counseller) #1-receive(children)
    utterance = db.Column(db.String(80))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user_id, date_YMD,date_YMDHMS, direction, utterance):
        self.date_YMD = date_YMD
        self.date_YMDHMS = date_YMDHMS
        self.direction = direction
        self.utterance = utterance

        self.user_id = user_id

    def json(self):
        return {'day': self.date_YMD,'time':self.date_YMDHMS[8:], 'direction': self.direction,'utterance':self.utterance}

    @classmethod
    def find_by_fulldate_with_user_id(cls, user_id, date):
        return cls.query.filter(and_(cls.user_id == user_id, cls.date_YMDHMS == date)).first()

    @classmethod
    def find_all_by_dateYMD_with_user_id(cls, user_id, date):
        return cls.query.filter(and_(cls.user_id == user_id, cls.date_YMD == date)).order_by(cls.id.desc()).all()

    @classmethod
    def find_range_with_user_id(cls, user_id, begin, latest):
        return cls.query.filter(and_(cls.date_YMD.between(begin,latest),cls.user_id == user_id)).order_by(cls.id.desc()).all()

    @classmethod
    def find_by_number_with_user_id(cls, user_id, latest,number):
        return cls.query.filter(and_(cls.date_YMDHMS < latest, cls.user_id == user_id)).order_by(cls.id.desc()).limit(number).all()

    @classmethod
    def find_all_by_user_id(cls,user_id):
        return cls.query.filter_by(user_id=user_id).order_by(cls.id.desc()).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
