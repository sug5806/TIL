from django.db import models


# Create your models here.

class AdminPage(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} {self.age} {self.address}'