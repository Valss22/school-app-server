from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]
