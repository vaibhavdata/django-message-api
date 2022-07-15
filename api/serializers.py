import re
from django.contrib.auth.hashers import check_password,make_password
from comman.MainService import MainService
from rest_framework import serializers, exceptions
from api.models import Account
from api.query import getUserByEmail,createUser


EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
PHONE_REGEX =r"(^[+0-9]{1,3})*([0-9]{10,11}$)"

class CreateUserSerlizer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    confirm_password  = serializers.CharField(required=True)
    #mobile  = serializers.CharField(required=True)


    class Meta:
        model = Account
        fields =['first_name','last_name','email','password','confirm_password']
    #field error message
    def __init__(self,*args,**kwargs):
        super(CreateUserSerlizer,self).__init__(*args,**kwargs)
        MainService.fieldRequiredMessage(self.fields)

    # Validations data
    def validation(self,data):
        errors ={}
        first_name = data.get('first_name',None)
        last_name = data.get('last_name',None)
        email = data.get('email',None)
        password = data.get('password',None)
        confirm_password = data.get('confirm_password',None)
        #mobile  = data.get('mobile',None)


        # validation error
        if first_name == "" or first_name is None:
            error ={
                "field" :"first_name",
                "message":"first name field value not here"
            }
            errors.append(error)
        if email == "" or email is None:
            error ={
                "field" :"email",
                "message":"email field value not here"
            }
            errors.append(error)
        if email or not re.match(EMAIL_REGEX,email):
            error = {
                "field": "email",
                "message": "email field value not here"
            }
            errors.append(error)

        if last_name == "" or last_name is None:
            error ={
                "field" :"last_name",
                "message":"last_name field value not here"
            }
            errors.append(error)
        if password == "" or password is None:
            error ={
                "field" :"password",
                "message":"password field value not here"
            }
            errors.append(error)
        if confirm_password == "" or confirm_password is None:
            error ={
                "field" :"confirm_password",
                "message":"confirm_password field value not here"
            }
            errors.append(error)
        if password != confirm_password:
            error = {
                "field": "password",
                "message": "password or   confirm_password not match "
            }
            errors.append(error)
        email = getUserByEmail(email)
        if email is not None:
            error = {
                "field": "email not get here",
                "message": "email not found in query "
            }
            errors.append(error)

        if len(errors)>0:
            raise  exceptions.ValidationError(errors)
        return data
    # create user
    def create(self,validate_data):
        userData = {
            "first_name":validate_data.get('first_name'),
            "last_name": validate_data.get('last_name'),
            "email" : validate_data.get('email'),
            "password":make_password(validate_data.get('password')),
            "confirm_password" : validate_data.get('confirm_password')
        }
        createUser(userData)
        return validate_data

class LoginUserSerlizer(serializers.ModelSerializer):
    email = serializers.CharField(allow_blank=False)
    password = serializers.CharField(allow_blank=False)

    class Meta:
        model = Account
        fields = ['email', 'password']

    # Fields Errors Message
    def __init__(self, *args, **kwargs):
        super(LoginUserSerlizer, self).__init__(*args, **kwargs)
        # Override field required and blank message
        MainService.fieldRequiredMessage(self.fields)

    # Validate request data
    def validation(self, data):
        errors = []

        email = data.get('email', '')
        password = data.get('password', '')

        user = getUserByEmail(email)
        if user is None:
            error = {"field": "email", "message": "email not found"}
            errors.append(error)
        elif password != '' or password is not None:
            if user is None or not check_password(password, user.password):
                error = {"field": "password", "message": "password not validation"}
                errors.append(error)
        if len(errors) > 0:
            raise exceptions.ValidationError(errors)
        return data

















