from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from .models import Insta
from django.shortcuts import redirect

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


class Instaupdate(UpdateView):
    model = Insta
    fields = ['text', 'image']
    template_name = 'photo/insta_update.html'



class Instadetail(DetailView):
    model = Insta
    template_name = 'photo/insta_detail.html'


