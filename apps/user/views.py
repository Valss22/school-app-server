from rest_framework.decorators import api_view
from rest_framework.request import Request
from . import services


@api_view(["POST"])
def register(request: Request):
    return services.create_user(request)
