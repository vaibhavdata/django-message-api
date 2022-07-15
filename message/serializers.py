from message.models import Message
from rest_framework import serializers, exceptions
from comman.MainService import MainService
from message.query import getUser,create_message
from api.serializers import CreateUserSerlizer
import re
from api.models import Account
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class MessageSerlizer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=True)
    class Meta:
        model = Message
        fields = ('id','date_created','date_updated','message','user')
        #depth = 1

        # Fields Errors Message
        def __init__(self, *args, **kwargs):
            super(MessageSerlizer, self).__init__(*args, **kwargs)
            # Override field required and blank message
            MainService.fieldRequiredMessage(self.fields)

        def validation(self, data):
            message = data.get('message','')
            return data





