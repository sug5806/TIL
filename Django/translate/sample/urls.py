from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('sample/', sample),
    path('language/<code>/', trans1),
]