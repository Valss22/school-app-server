from django.contrib import admin
from django.urls import path
from apps.user.views import user_router
from ninja import NinjaAPI

api = NinjaAPI()

api.add_router("users/", user_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
]
