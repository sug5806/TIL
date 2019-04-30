from django.contrib import admin

from .models import Bookmark


# Register your models here.
# 관리자 페이지에서 관리할 모델을 등록
# 관리자 페이지를 커스터마이징
# 옵션 클래스를 만들어서 추가

class BookmarkOptions(admin.ModelAdmin):
    # DB의 필드명과 동일해야함
    list_display = ['id', 'site_name', 'url']

    # 아무곳이나 적용하면 안됨, 어지간하면 적용안함
    # list_editable = ['site_name','url']

    # 대부분 DateTime 필드가 있을 경우 많이 사용
    # list_filter = ['url']

    # ForeignKey 필드같은 다른 테이블을 참조하는 항목은 검색 불가
    search_fields = ['site_name']
    # raw_id_fields : 선택값을 입력값으로 바꿔줌
    # 관리자 페이지에 커스텀 페이지 추가
    # 관리자 페이지에 action 추가


# Bookmark를 관리할때 BookmarkOptions라는 옵션을 추가하겠다.
admin.site.register(Bookmark, BookmarkOptions)
