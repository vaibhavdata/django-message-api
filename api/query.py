from api.models import Account
from django.db.models import Q
from django.utils.timezone import datetime # important if using timezones
today = datetime.today()

def getUserByEmail(email:str):
    try:
        user = Account.objects.filter(email=email).first()
    except Exception as e:
        user = None
    return user
def createUser(data : dict):
    try:
        user = Account()
        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        user.email = data.get("email")
        user.password = data.get("password")
        user.confirm_password = data.get("confirm_password")
        user.save()
    except Exception as e:
        user = None
    return user


