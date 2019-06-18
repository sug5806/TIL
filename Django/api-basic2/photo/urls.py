from django.urls import path
from .views import *

app_name = 'photo'

urlpatterns = [

    path('list/', PhotoList.as_view(), name='list'),
    path('create/', PhotoCreate.as_view(), name='create'),
    path('detail/<int:pk>/', PhotoDetail.as_view(), name='detail'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name='delete'),
]