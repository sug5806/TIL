from django.urls import path

from .views import BookmarkDetail, BookmarkDelete, BookmarkCreate, BookmarkUpdate, BookmarkList

# namespace = 이름 공간
# 다른 앱들과 url pattern 이름이 겹치는 것을 방지하기 위해서 사용
# 2.x버전 이전에는 namespace라는 인수가 존재
app_name = 'bookmark'
urlpatterns = [
    # 함수형 뷰 : 이름만 쓴다
    # 클래스형 뷰 : 이름.as_view()
    path('', BookmarkList.as_view(), name='index'),
    path('create/', BookmarkCreate.as_view(), name='crate'),
    path('delete/<int:pk>/', BookmarkDelete.as_view(), name='delete'),
    path('update/<int:pk>/', BookmarkUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', BookmarkDetail.as_view(), name='detail'),
]
