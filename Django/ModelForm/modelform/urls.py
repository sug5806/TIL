from django.urls import path
from .views import (
    list_create_product,
)

app_name = 'modelform'

urlpatterns = [
    path('', list_create_product, name='list_create_product')
]