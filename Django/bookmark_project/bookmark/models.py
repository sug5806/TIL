from django.db import models


# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=50)
    url = models.URLField()

    created = models.DateTimeField(auto_now_add=True)

    # DB에 적용 : makemigrations, migrate
    # python manage.py makemigrations bookmark
    # python manage.py migrate bookmark 0001

    def __str__(self):
        return "Site name : " + self.site_name + ", URL : " + self.url

    # 메타 클래스는 옵션 클래스 -> 내가 상속을 받았는데, 속성값에 변경이 필요하다면 사용
    class Meta:
        # 정렬 : 필드값 -> 필드값 오름차순, -필드이름 -> 필드값 내림차순
        ordering = ['site_name']
