from django.urls import path

from .views import *

urlpatterns = [
    path('', TweetListCreateView.as_view()),
    path('<int:pk>/', TweetDetailView.as_view()),
]