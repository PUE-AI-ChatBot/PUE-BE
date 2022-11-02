import json

from db import db
from models import and_

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    user_subname = db.Column(db.String(80))
    password = db.Column(db.String(80))
    user_name = db.Column(db.String(80))

    provider = db.Column(db.String(80))
    pid = db.Column(db.String(80))

    make_date = db.Column(db.String(80))
    num_of_userchats =  db.Column(db.Integer())
    num_of_counselling = db.Column(db.Integer())

    chats = db.relationship('ChatModel', backref='users')
    statistics = db.relationship('StatisticModel', backref='users')

    def __init__(self, user_subname,make_date,user_name="",password="",provider="",pid=""):
        self.user_subname = user_subname
        self.make_date = make_date
        self.user_name = user_name
        self.password = password
        self.provider = provider
        self.pid = pid
        self.num_of_userchats = 0
        self.num_of_counselling = 0

    def json(self):
        return {
            "info":{
                'id':self.id,
                'user_name':self.user_name,
                'user_subname':self.user_subname,
                'provider':self.provider,
            }
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user_name):
        return cls.query.filter_by(user_name=user_name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_oauth_by_pid(cls, pid,oauth):
        return cls.query.filter(and_(cls.pid == pid,cls.provider == oauth)).first()
