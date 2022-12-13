from ninja import NinjaAPI

users_api = NinjaAPI()


@users_api.get("/users/hello")
def login(request):
    return {"message": "Hello World"}
