from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from api.serializers import CreateUserSerlizer,LoginUserSerlizer
from api.query import createUser,getUserByEmail
from rest_framework.authtoken.models import Token
from comman.MainService import MainService,StatasType
# Create your views here.
@swagger_auto_schema(
    method='post',
    request_body=CreateUserSerlizer,
    responses=MainService.responseData()
)
@api_view(['POST'])
def register(request):
    resData = {}
    serializer = CreateUserSerlizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        email = serializer.data['email']
        user = getUserByEmail(email)

        #token = MainService.getJwtToken("ACCESS_TOKEN",user)
        token = Token.objects.get(user=user).key
        resData['status'] = StatasType.success.value
        #resData['data'] = {
           # "access_token": token.get('access_token'),
        #}
        resData['token']=token
        resData['message'] = "user register succesfully"
        resData['errors'] = []
        status_code = 201
    else:
        # Make response data fail case
        res = MainService.setException(serializer)
        resData['status'] = StatasType.errror.value
        resData['data'] = {}
        resData['message'] = res.get('message')
        resData['errors'] = res.get('errors')
        status_code = 200
    return Response(resData,status=status_code)

@swagger_auto_schema(
    method='post',
    request_body=LoginUserSerlizer,
    responses=MainService.responseData()
)
@api_view(['POST'])
def login(request):
    resData = {}
    serializer = LoginUserSerlizer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        user = getUserByEmail(email)
        #token = MainService.getJwtToken("ACCESS_TOKEN", user)
        token = Token.objects.get(user=user).key
        resData['status'] = StatasType.success.value
        '''resData['data'] = {
            "access_token": token.get('access_token'),
        }'''
        resData['token']=token
        resData['message'] = "user login sussesfully"
        resData['errors'] = []
        status_code = 201
    else:
        res = MainService.setException(serializer)
        resData['status'] = StatasType.errror.value
        resData['data'] = {}
        resData['message'] = res.get('message')
        resData['errors'] = res.get('errors')
        status_code = 200
    return Response(resData, status=status_code)


