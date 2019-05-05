from django.db import models

# from django.contrib.auth import get_user_model
# 커스텀할때 이것을 사용하는것이 좋다

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# User모델은 확장 가능
# settings.AUTH_USER_MODEL

from django.urls import reverse
# get_absloute_url을 사용하기 위함
# reverse : url pattern 이름을 가지고 주소를 만들어주는 함수

from django.http import HttpResponseRedirect

# Create your models here.
# 기본 모델
"""

작성자 : author
본문글 : text
사진 : image
작성일 : created
수정일 : updated
+ tag, like
-- 별도 기능으로 comment

"""

class Insta(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name='photos')
           # models.ForeignKey(get_user_model(), )
    # author = models.ForeignKey(연결되는 모델, 삭제시 동작, 연관 이름)
    # CASCADE : 유저가 탈퇴하면 사진도 싹 지운다.
    # PROTECT : 사진을 다 안지우면 너 탈퇴 안됨 - 탈퇴 프로세스에 사진을 우선 삭제하고 탈퇴 시킨다.
    # 특정값으로 세팅 : 탈퇴시키고 특정값으로 재설정
    # related_name으로 연관 데이터를 얻을 수 없다면 쿼리를 별도로 실행해야 한다.
    # 내 프로필 페이지 - 내가 올린 사진만 뜬다

    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    # upload_to는 함수를 사용해서 폴더를 동적으로 설정할 수 있다.

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    like = models.ManyToManyField(User, related_name='like_post', blank=True)
####

    save = models.ManyToManyField(User, related_name='save_post', blank=True)

####
    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        # detail/<int:pk>/ pk에 들어갈 값을 args로 전달함
        return reverse('photo:detail', args=[self.id])

