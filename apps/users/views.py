from ninja import NinjaAPI
from .schemas import UserIn
from django.contrib.auth.models import User
from ninja import Router

# class AuthBearer(HttpBearer):
#     def authenticate(self, request, token):
#         if token == "supersecret":
#             return token


user_router = Router(tags=["users"])


@user_router.post("/login")
def login(request, user: UserIn):
    pass
    # User.objects.create_user(**user.dict())
    # return {"token": request.auth}
