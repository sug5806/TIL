from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    # message와 profile 필드를 커스텀으로 추가시킨다.
    message = models.TextField(blank=True)
    profile = models.ImageField(upload_to='profile/%Y/%m/%d', blank=True)