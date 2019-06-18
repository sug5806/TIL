from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework import generics

from .models import Photo
from .serializers import *


# Create your views here.
class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'


class PhotoCreate(CreateView):
    model = Photo
    template_name = 'photo/photo_create.html'
    fields = ['image', 'text']

    def form_valid(self, form):
        if self.request.user.id:
            form.instance.author_id = self.request.user.id
            return super().form_valid(form)
        else:
            return False

    # get_absolute_url 이 있으므로 생략 가능
    # success_url = '/'


class PhotoDetail(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'


class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['image', 'text']
    template_name = 'photo/photo_update.html'


class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'


######################################################
class PhotoListAPI(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer


class PhotoCreateAPI(generics.CreateAPIView):
    serializer_class = PhotoCreateSerializer


class PhotoDetailAPI(generics.RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer


class PhotoUpdateAPI(generics.UpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoUpdateSerializer


class photoDeleteAPI(generics.DestroyAPIView):
    queryset = Photo.objects.all()

# 토큰 인증 기능 추가, 기본 인증, 권한 클래스

# 1) 인증된 사용자만 API를 사용할 수 있도록 설정 : token 인증
# 2) 특정 동작에 대해 특정 권한을 득한 사용자만 사용할 수 있도록 설정 : permission클래스 추가
