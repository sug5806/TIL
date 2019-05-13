from django.urls import path

from .views import *

app_name = 'board'

urlpatterns = [
    path('', document_list, name='list'),
    path('create/', document_create, name='create'),
    path('update/<int:document_id>/', document_update, name='update'),
    path('delete/<int:document_id>/', document_delete, name='delete'),
    # 클래스형 뷰에서는 pk 였던 이유가 pk로 받아서 그런것이다
    path('detail/<int:document_id>/', document_detail, name='detail'),
]
