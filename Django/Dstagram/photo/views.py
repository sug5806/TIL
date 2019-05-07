# Create your views here.
# CRUDL - 이미지를 띄우는 방법
# 제네릭 뷰
# 쿼리셋 변경하기, context_data 추가하기, 권한 채크
# 함수형 뷰 <-> 클래스형 뷰

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Photo


class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'


from django.shortcuts import redirect


class PhotoCreate(CreateView):
    model = Photo
    fields = ['image', 'text']
    template_name = 'photo/photo_create.html'
    success_url = '/'

    def form_valid(self, form):
        # 입력된 자료가 올바른지 채크
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 올바르다면
            # form : 모델 폼
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form': form})


class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['image', 'text', ]
    template_name = 'photo/photo_update.html'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            # message.tag
            messages.warning(request, '수정할 권한이 없습니다.')
            return HttpResponseRedirect(object.get_absolute_url())
        else:
            super(PhotoUpdate, self).dispatch(request, *args, **kwargs)


class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = '/'

    # Life Cycle - iOS, Android, Vue, React, Django, Rails
    # Framework 는 라이프 사이클이 존재 : 어떤 순서로 구동이 되느냐?
    # URLConf -> View -> Model 순으로
    # 어떤 뷰를 구동할 때 그 안에서 동작하는 순서

    # 사용자가 접속했을 때 get이냐? post? 등을 결정하고 분기하는 부분
    # def dispatch(self, request, *args, **kwargs):
    #     pass

    # 로직을 수행하고, 템플릿을 랜더링 한다.

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.author != request.user:
            messages.warning(request, '삭할 권한이 없습니다.')
            return HttpResponseRedirect(object.get_absolute_url())
        else:
            super(PhotoUpdate, self).dispatch(request, *args, **kwargs)


class PhotoDetail(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'


from django.views.generic.base import View
from django.http import HttpResponseForbidden


class PhotoLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk=photo_id)
                user = request.user
                if user in photo.like.all():
                    photo.like.remove(user)
                else:
                    photo.like.add(user)
            return HttpResponseRedirect('/')
