from rest_framework.decorators import api_view
from rest_framework.request import Request
from . import services
from typing import TypedDict


class UserIn(TypedDict):
    first_name: str
    last_name: str
    password: str


def request_validator(schema):
    def inner(func):
        def wrapper(request: Request):
            print(schema)
            print(request.data)
            return func(request)

        return wrapper

    return inner


@api_view(["POST"])
@request_validator(UserIn)
def register(request: Request):
    return services.create_user(request)
