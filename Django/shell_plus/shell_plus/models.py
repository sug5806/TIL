from django.db import models


# Create your models here.

class Child(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=50)
    parent = models.ForeignKey('Parent', models.CASCADE, related_name='child')

    def __str__(self):
        return f'{self.name} {self.age} {self.address} {self.parent}'


class Parent(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'