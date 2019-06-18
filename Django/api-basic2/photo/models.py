from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Photo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username + " photo on " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        ordering = ['-updated', '-created']