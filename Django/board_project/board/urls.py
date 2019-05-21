from django.urls import path

from .views import *

app_name = 'board'

urlpatterns = [
    path('', document_list, name='list'),
    path('aj', get_data_list, name='aj'),
    path('search/', search_list, name='search'),
    path('create/', document_create, name='create'),
    path('comment/create/<int:document_id>/', comment_create, name='comment_create'),
    path('comment/update/<int:comment_id>/', comment_update, name='comment_update'),
    path('comment/delete/<int:comment_id>/', comment_delete, name='comment_delete'),
    path('update/<int:document_id>/', document_update, name='update'),
    path('delete/<int:document_id>/', document_delete, name='delete'),
    # 클래스형 뷰에서는 pk 였던 이유가 pk로 받아서 그런것이다
    path('detail/<int:document_id>/', document_detail, name='detail'),

    # AJAX 연결
    path('ajax/get_data/', get_data_ajax, name='get_data_ajax'),
]
