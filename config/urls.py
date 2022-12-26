from django.contrib import admin
from django.urls import path
from apps.user import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", views.register),
]
