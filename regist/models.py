from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
# {
#     "username": "artem",
#     "email": "nikolayvaganov2@gmail.com",
#     "password" : "12345678"
# }

class UserManager(BaseUserManager):
    def create_user(self, email):
        user = self.model(email=self.normalize_email(email))
        user.save()

        return user

    def create_superuser(self, email):
        user = self.create_user(email)

        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    money = models.IntegerField(default=10000000)
    power = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()