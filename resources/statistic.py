from flask_restful import Resource, reqparse
from models.statistic import StatisticModel,init_emotion
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from datetime import datetime, timedelta

class WeekEmotion(Resource):
    def get(self):

        user_id = 1
        total_cnt = 0
        today = datetime.now().strftime('%Y%m%d')

        ret_emotions = init_emotion.copy()
        stats = StatisticModel.find_by_number_with_user_id(user_id,today,30)

        if not stats :
            return {
                'weather' : "중립",
                'summary': []
               }

        for stat in stats:
            temp = json.loads(stat.emotions)
            total_cnt += stat.total
            for key in ret_emotions.keys():
                ret_emotions[key] += temp[key]

        max_key = max(ret_emotions, key=ret_emotions.get)

        return {
               'weather': max_key,
               'summary': {
                   "total": total_cnt,
                   'emotions': ret_emotions
                   }
               }, 200


class NumberStatList(Resource):
    def get(self,date, number):

        user_id = 1

        stats = StatisticModel.find_by_number_with_user_id(user_id,date,number)
        return {
                "statistics" : [stat.json() for stat in stats]
            }, 200

class SummaryNumberStatList(Resource):
    def get(self,date, number):

        user_id = 1
        total_cnt=0

        ret_emotions = init_emotion.copy()
        stats = StatisticModel.find_by_number_with_user_id(user_id,date,number)

        if not stats :
            return {
                'isSummary':False,
                "summary":[]
               }

        for stat in stats:
            temp = json.loads(stat.emotions)
            total_cnt += stat.total
            for key in ret_emotions.keys():
                ret_emotions[key] += temp[key]


        return {
                'isSummary':True,
                   'summary':{
                        "total":total_cnt,
                        'emotions': ret_emotions
                    }
               }, 200



class RangeStatList(Resource):
    def get(self,end,begin):
        user_id = 1
        stats = StatisticModel.find_range_with_user_id(user_id, begin, end)

        return {
                   "statistics": [stat.json() for stat in stats]
               }, 200

class SummaryRangeStatList(Resource):
    def get(self,end,begin):
        user_id = 1
        total_cnt = 0

        ret_emotions = init_emotion.copy()
        stats = StatisticModel.find_range_with_user_id(user_id, begin, end)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        for stat in stats:
            temp = json.loads(stat.emotions)
            total_cnt += stat.total
            for key in ret_emotions.keys():
                ret_emotions[key] += temp[key]

        return {
                   'isSummary': True,
                   'summary': {
                       "total": total_cnt,
                       'emotions': ret_emotions
                   }
               }, 200

class YMDStatList(Resource):
    def get(self,day):
        user_id = 1

        stat = StatisticModel.find_by_dateYMD_with_user_id(user_id,day)

        if not stat :
            return {
                "statistics": []
            }

        return {
                   "statistics" : [stat.json()]
               }, 200
