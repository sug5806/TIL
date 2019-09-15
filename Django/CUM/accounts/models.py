from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    message = models.TextField(blank=True)
    profile = models.ImageField(upload_to='user_image/profile/%Y/%m/%', blank=True)