from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework.response import Response
from django.core import exceptions


def check_user_in_db(request: Request):
    try:
        User.objects.get(**request.data)
    except exceptions.ObjectDoesNotExist:
        return Response({"msg": "User doesn't exists"})


def create_user(request: Request):
    pass
    ##User.objects.create_user(**request.data)
