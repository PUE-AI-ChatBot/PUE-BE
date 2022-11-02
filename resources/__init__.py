from packages.pue_AI.aimodel import AIModel

main_ai = AIModel()

def create_api(api):
    from .user import UserRegister, User, UserLogin, UserProfile
    from .chat import RangeChatList, AllChatList,YMDChatList,OneChat,NumberChatList
    from .statistic import RangeStatList, YMDStatList, NumberStatList, SummaryRangeStatList, YMDStatList, SummaryNumberStatList, WeekEmotion
    from .oauth import GoogleLogin,KakaoLogin
    from .develop import MakeMock

    #dev
    api.add_resource(MakeMock, '/make-mock')

    #belonged to chat
    api.add_resource(NumberChatList,'/chats/number/latest/<string:date>/before/<int:number>')
    api.add_resource(RangeChatList, '/chats/range/latest/<string:end>/from/<string:begin>')
    api.add_resource(YMDChatList, '/chats/day/<string:day>')
    api.add_resource(OneChat, '/chat/<string:date>')

    #belonged to chart
    api.add_resource(NumberStatList, '/stat/number/latest/<string:date>/before/<int:number>')
    api.add_resource(RangeStatList, '/stat/range/latest/<string:end>/from/<string:begin>')
    api.add_resource(YMDStatList, '/stat/day/<string:day>')

    # belonged to summary chart
    api.add_resource(SummaryNumberStatList, '/stat/summary/number/latest/<string:date>/before/<int:number>')
    api.add_resource(SummaryRangeStatList, '/stat/summary/range/latest/<string:end>/from/<string:begin>')

    # belonged to utils
    api.add_resource(WeekEmotion, '/stat/week-emotion')
    api.add_resource(UserProfile,'/user/profile')

    #belonged to USER
    api.add_resource(UserRegister, '/register')
    api.add_resource(User, '/user')
    api.add_resource(UserLogin, '/login')

    #belonged to OAuth
    api.add_resource(GoogleLogin, '/login/google')
    api.add_resource(KakaoLogin,'/login/kakao')


def create_socketio(sock):
    from .chatnamespace import ChatNamespace
    sock.on_namespace(ChatNamespace('/realchat'))


