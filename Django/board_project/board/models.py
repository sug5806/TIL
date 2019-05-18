from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

# 하나의 웹사이트
class Board(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30, db_index=True, unique=True, allow_unicode=True, blank=True)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return self.name

class Category(models.Model):
    board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30, db_index=True, unique=True, allow_unicode=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=200, blank=True)

    class Meta:
        # DB에 기본적으로 설정될 정렬값
        ordering = ['slug']

    def __str__(self):
        return self.name





class Document(models.Model):
    board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True)
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
        return self.title


    def get_absolute_url(self):
        return reverse("board:detail", args=[self.id])



class Comment(models.Model):
    # Todo : 댓글 남기기를 위해서 Form 필요
    # Todo : 뷰 처리는 Document의 뷰에서 처리
    # document 입장에서 부르는 이름이 related_name / Document에는 comments라는 필드가 생리
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='comments')

    # 작성자 입장에서의 comments
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    text = models.CharField(max_length=255)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    like = models.PositiveIntegerField(default=0) # ManyToMany
    dislike = models.PositiveIntegerField(default=0) # ManyToMany

    def __str__(self):
        return (self.author.username if self.author else "무명") + "의 댓글"