from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   message = models.TextField(blank=True)
   profile = models.ImageField(upload_to='user_image/profile/%Y/%m/%d', blank=True)