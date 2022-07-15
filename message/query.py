from api.models import Account
from message.models import Message
from django.db.models import Q
from django.utils.timezone import datetime
from rest_framework.throttling import UserRateThrottle,ScopedRateThrottle,BaseThrottle

def getUser(user:str):
    try:
        user = Account.objects.filter(email=user).first()
    except Exception as e:
        user = None
    return user
def create_message(data : dict):
    try:
        message = Message()
        message.message = data.get("message")
        #message.user = data.get("user")
        message.save()
    except Exception as e:
        message = None
    return message


class CustomRateThrottle(UserRateThrottle):
    scope = 'message_post'
class CustomMinThrottle(UserRateThrottle):
    scope = "message_day"
