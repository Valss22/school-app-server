from django.contrib import admin
from django.urls import path
from apps.users.views import users_api


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", users_api.urls),
]
