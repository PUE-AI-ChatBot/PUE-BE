from flask_restful import Resource, reqparse
from models.statistic import StatisticModel,init_emotion
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from datetime import datetime, timedelta

class NumberStatList(Resource):
    @jwt_required()
    def get(self,date, number):

        user_id = get_jwt_identity()
        total_cnt=0

        end = datetime.strptime(date, '%Y%m%d')
        begin = (end - timedelta(number-1)).strftime("%Y%m%d")

        ret_emotions = init_emotion.copy()
        stats = StatisticModel.find_range_with_user_id(user_id, begin, date)

        if not stats :
            return {'message': 'No statistics...'}, 400

        for stat in stats:
            temp = json.loads(stat.emotions)
            for key in ret_emotions.keys():
                ret_emotions[key] += temp[key]
                total_cnt += temp[key]

        return {'total':total_cnt,'statistics': ret_emotions}, 200

class RangeStatList(Resource):
    @jwt_required()
    def get(self,end,begin):
        user_id = get_jwt_identity()
        total_cnt = 0

        ret_emotions = init_emotion.copy()
        stats = StatisticModel.find_range_with_user_id(user_id, begin, end)

        if not stats :
            return {'message': 'No statistics...'}, 400

        for stat in stats:
            temp = json.loads(stat.emotions)
            for key in ret_emotions.keys():
                ret_emotions[key] += temp[key]
                total_cnt += temp[key]

        return {'total':total_cnt,'statistics': ret_emotions}, 200

class YMDStatList(Resource):
    @jwt_required()
    def get(self,day):
        user_id = get_jwt_identity()

        total_cnt=0
        stat = StatisticModel.find_by_dateYMD_with_user_id(user_id,day)

        if not stat :
            return {'message': 'No statistics...'}, 400

        temp = json.loads(stat.emotions)

        for key in temp.keys():
            total_cnt += temp[key]

        return {'total':total_cnt,'statistics': temp},200

class AllStatList(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()

        total_cnt = 0
        ret_emotions = init_emotion.copy()
        stats = StatisticModel.find_by_user_id(user_id)

        if not stats :
            return {'message': 'No statistics...'}, 400

        for stat in stats:
            temp = json.loads(stat.emotions)
            for key in ret_emotions.keys():
                ret_emotions[key] += temp[key]
                total_cnt += temp[key]

        return {'total':total_cnt,'statistics': ret_emotions}, 200