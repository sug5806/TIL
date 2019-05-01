from .views import Instalist, Instacreate, Instadelete, Instadetail, Instaupdate
from django.urls import path

app_name = 'photo'
urlpatterns = [
    path('', Instalist.as_view(), name='list'),
    path('create/', Instacreate.as_view(), name='create'),
    path('update/<int:pk>', Instaupdate.as_view(), name='update'),
    path('delete/<int:pk>', Instadelete.as_view(), name='delete'),
    path('detail/<int:pk>', Instadetail.as_view(), name='detail'),


]



