from django.urls import path
from .views import fbv_post

app_name = 'fbv'

urlpatterns = [
    path('', fbv_post, name='fbv_post'),
]