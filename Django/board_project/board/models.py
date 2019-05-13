from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

# class Board(models.Model):
#     pass

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30, db_index=True, unique=True, allow_unicode=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=200, blank=True)

    class Meta:
        # DB에 기본적으로 설정될 정렬값
        ordering = ['slug']

    def __str__(self):
        return self.name + " " + self.slug



class Document(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='documents')

    # User 모델을 커스텀한 경우, 불러다 써야한다
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, db_index=True, unique=True, allow_unicode=True, blank=True)
    text = models.TextField()
    # upload_to 동적으로 경로 설정 가능
    image = models.ImageField(upload_to='board_images/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author + " " + self.title + " " + self.created + " " + self.updated
