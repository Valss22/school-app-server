from ninja import NinjaAPI
from .schemas import UserIn
from django.contrib.auth.models import User
from ninja.security import HttpBearer


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


users_api = NinjaAPI()


@users_api.post("/users/hello")
def login(request, user: UserIn, auth=AuthBearer()):
    # User.objects.create_user(**user.dict())
    return {"token": request.auth}
