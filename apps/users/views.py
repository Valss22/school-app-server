from .schemas import UserIn, UserOut
from ninja import Router
from ninja.security import HttpBearer
from . import services


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


user_router = Router(tags=["users"])


@user_router.post("/login", response=UserOut)
def login(request, user: UserIn):
    return services.login_user(request, user)
