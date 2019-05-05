from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from .models import Insta
from django.shortcuts import redirect

from django.contrib.auth import get_user_model

from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

class Instacreate(CreateView):
    model = Insta
    fields = ['text', 'image']
    template_name = 'photo/insta_create.html'
    success_url = '/'

    def form_valid(self, form):
        # 입력된 자료가 올바른지 체크
        form.instance.author_id = self.request.user.id
        # 올바르다면
        # form : 모델 폼
        # 외래키 필드명_id
        # self.request.user : 현재 로그인한 유저

        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            # 올바르지 않다면
            return self.render_to_response({'form' : form})


class Instalist(ListView):
    model = Insta
    template_name = 'photo/insta_list.html'


class Instadelete(DeleteView):
    model = Insta
    template_name = 'photo/insta_delete.html'
    success_url = '/'


    # 다른유저가 내 게시물 접근 못하게 하기
    # 방법 1 : html파일에서 하기
    # 방법 2 : dispath 등등

    # Life Cycle - iOS, Android, Vue, React, Django, Rails
    # Framework는 라이프 사이클이 존재 : 어떤 순서로 구동이 되느냐?
    # URLConf -> View -> Model(View에서 DB가 필요하다면) 순으로 동작
    # 어떤 뷰를 구동할 때 그 안에서 동작하는 순서


    def dispatch(self, request, *args, **kwargs):
        # 사용자가 접속했을 때 get이냐? post? 등을 결정하고 분기하는 부분
        obj = self.get_object()
        if self.request.user != obj.author:
            messages.info(request, 'Fail Delete! 권한이 없습니다')
            return redirect('/')
        messages.info(request, 'Successfully Delete!')
        return super(Instadelete, self).dispatch(request, *args, **kwargs)


    # get, post : 로직을 수행하고, 템플릿을 랜더링 한다.
    # view를 만들때마다 get과 post를 별도로 만들어야한다.
    # dispatch로만 할수는 없다. Ex) delete를 get형식으로만 해야한다

    # def get(self, request, *args, **kwargs):
    #     object = self.get_object()
    #     if object.author != request.user:
    #         messages.warning(request, "삭제할 권한이 없습니다.")
    #
    #         return redirect('/')
    #         # return HttpResponseRedirect(object.get_absolute_url())
    #         # 삭제 페이지에서 권한이 없다!
    #         # 원래 디테일 페이지로 돌아가서 삭제에 실패했습니다.
    #
    #     else:
    #         return super(PhotoDelete, self).get(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     object = self.get_object()
    #     if object.author != request.user:
    #         messages.warning(request, "삭제할 권한이 없습니다.")
    #         return HttpResponseRedirect(object.get_absolute_url())
    #
    #     else:
    #         return super(PhotoDelete, self).get(request, *args, **kwargs)



    # def get_object(self, queryset=None):
    #     # 해당 쿼리셋을 이용해서 현재 페이지에 필요한 object를 인스턴스화 한다.
    #     pass
    #
    # def get_queryset(self):
    #     # 어떻게 데이터를 가져올 것이냐?
    #     pass




class Instaupdate(UpdateView):
    model = Insta
    fields = ['text', 'image']
    template_name = 'photo/insta_update.html'

    def dispatch(self, request, *args, **kwargs):
        # 저장된 게시글의 사용자이름을 가져옴
        obj = self.get_object()
        if self.request.user != obj.author:
            messages.info(request, 'Fail Update! 권한이 없습니다')
            return redirect('/')
        return super(Instaupdate, self).dispatch(request, *args, **kwargs)


class Instadetail(DetailView):
    model = Insta
    template_name = 'photo/insta_detail.html'


from django.views.generic.base import View
from django.http import HttpResponseForbidden

class Instalike(View):
    def get(self, request, *args, **kwargs):
        # Like를 할 정보가 있다면 진행, 없다면 중단
        if not request.user.is_authenticated:
            return HttpResponseForbidden
        else:

            # 1. 어떤 포스팅?
            # url : www.naver.com/blog/like/?photo_id=1
                # request.GET.get('photo_id')
            # url : www.naver.com/blog/like/1/
                # kwargs['photo_id']
                # path('blog/like/<int:photo_id>/')
            # 2. 누가?
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Insta.objects.get(pk=photo_id)
                user = request.user
                if 'photo_id' in user.like.all():
                    photo.like.remove(user)
                else:
                    photo.like.add(user)
            return HttpResponseRedirect('/')
