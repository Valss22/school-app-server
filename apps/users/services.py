from .schemas import UserIn
from django.contrib.auth.models import User


def login_user(request, user: UserIn):
    user = User.objects.get(**user.dict())
    return user
