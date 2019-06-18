from django.shortcuts import render


from django.views.generic import ListView
from rest_framework import generics
from .serializers import *

# Create your views here.


from .models import Photo


class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'


class PhotoListAPI(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer