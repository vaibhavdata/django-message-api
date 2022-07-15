import enum
from api.models import Account
from django.contrib.sites.shortcuts import get_current_site
import hashlib
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg import openapi
import datetime
import time
import os
import random, math
from django.core.files.storage import FileSystemStorage
from math import radians, cos, sin, asin, sqrt
from comman.message import ValidationMessages
class StatasType(enum.Enum):
    success = "Success"
    errror = "Error"
    fail = "Fail"

class MainService:


    @staticmethod
    def emailValidation():
        return r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    @staticmethod
    def responseData():
        data = {
            200 : openapi.Schema(
                type = openapi.TYPE_STRING,
                status = "Success",
                data = openapi.TYPE_OBJECT,
                message = openapi.TYPE_STRING
            ),
            400 : openapi.Schema(
                type = openapi.TYPE_STRING,
                status = "Success",
                data = openapi.TYPE_OBJECT,
                message = openapi.TYPE_STRING
            )
        }
        return data

    @staticmethod
    def getJwtToken(typeName, user):
        refresh = RefreshToken.for_user(user)
        data = {}
        if typeName == 'ACCESS_TOKEN':
            data['access_token'] = str(refresh.access_token)
        else:
            data['refresh_token'] = str(refresh)
        return data
    @staticmethod
    def fieldRequiredMessage(fields):
        for field in fields:
            fields[field].error_messages["required"] = ValidationMessages.the.value + ' ' + \
                                                       field.replace('_', ' ') + ' ' + \
                                                       ValidationMessages.field_is_required.value.lower()
            fields[field].error_messages["blank"] = ValidationMessages.the.value + ' ' + \
                                                    field.replace('_', ' ') + ' ' + \
                                                    ValidationMessages.field_is_required.value.lower()

    @classmethod
    def setException(cls, serializer):
        errors = []
        message = ''
        for error in serializer.errors:
            if error == "non_field_errors":
                data = serializer.errors[error][0]
                errors.append(data)
                message = cls.addString(message, serializer.errors[error][0])
            else:
                data = {
                    "field": error,
                    "message": serializer.errors[error][0]
                }
                errors.append(data)
                message = cls.addString(message, serializer.errors[error][0])
        data = {
            "errors": errors,
            "message": message
        }
        return data

    @staticmethod
    def addString(string, value):
        if string:
            if type(value) == dict:
                string = string + ', ' + value.get('message')
            else:
                string = string + ', ' + value
        else:
            if type(value) == dict:
                string = value.get('message')
            else:
                string = value
        return string



