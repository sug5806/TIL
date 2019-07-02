from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, related_name='entrys', on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.headline




