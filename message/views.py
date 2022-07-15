from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from message.serializers import MessageSerlizer
from message.models import Message
from comman.MainService import MainService,StatasType
from api.models import Account
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import (api_view, authentication_classes,
permission_classes,throttle_classes)
from .query import getUser,CustomRateThrottle,CustomMinThrottle
from rest_framework.response import Response

@swagger_auto_schema(
    method='post',
    request_body=MessageSerlizer,
    responses=MainService.responseData()
)
@api_view(['POST'])
@throttle_classes([CustomRateThrottle,CustomMinThrottle])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def message(request):
    resData ={}
    user = request.user

    serilize = MessageSerlizer(data=request.data)
    if serilize.is_valid():
        serilize.save(user = request.user)
        data = serilize.data
        print(data)


        resData['status'] = StatasType.success.value
        resData['data'] = {
            "id": data["id"],
            "date_created": data['date_created'],
            "date_updated":data["date_updated"],
            "message": data['message'],
            "creted_by" :{
                "id":user.id,
                "email" : user.email,
                "user name": user.first_name,


            }
        }
        resData['message'] = "message"
        resData['errors'] = []
        status_code = 201
    else:
        # Make response data fail case
        res = MainService.setException(serilize)
        resData['status'] = StatasType.errror.value
        resData['data'] = {}
        resData['message'] = res.get('message')
        resData['errors'] = res.get('errors')
        status_code = 200
    return Response(resData, status=status_code)


