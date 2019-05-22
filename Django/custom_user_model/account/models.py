from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.contrib.auth.models import AbstractUser

# 클래스 이름은 무관
class User(AbstractUser):
    message = models.TextField(blank=True)
    profile = models.ImageField(upload_to='user_images/profile/%Y/%m/%d', blank=True)
