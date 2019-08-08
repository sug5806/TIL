from django.urls import path

from .views import *

app_name = 'polls'

urlpatterns = [
    # 함수형 뷰
    # path('', index, name='index'),
    # path('<int:question_id>/', detail, name='detail'),
    # path('<int:question_id>/results/', results, name='results'),
    # path('<int:question_id>/vote/', vote, name='vote'),

    # 클래스형 뷰
    path('', IndexView.as_view(), name='index'),
    path('<pk>/', Detail_View.as_view(), name='detail'),
    path('<int:pk>/result/', ResultsView.as_view(), name='result'),
    path('<int:question_id>/vote/', vote, name='vote'),
]