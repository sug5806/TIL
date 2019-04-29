from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

# 클래스형 뷰의 이름은 자유
from .models import Bookmark


class BookmarkList(ListView):
    model = Bookmark
    # _list

    # 템플릿 종류를 바꾸거나 읽어오는 데이터,문
    # 페이지네이션을 걸거나 검색 쿼리를 적용, 권한체크


# 뷰를 만들었다 -> url연결

class BookmarkCreate(CreateView):
    model = Bookmark
    # fileds는 사용자가 입력할 모델 필드를 정하는 것
    # DB에서 지정한 필드명과 동일해야 하는듯?
    fields = ['site_name', 'url']
    template_name_suffix = '_create'
    success_url = '/'
    # _create
    # _form


class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name_suffix = '_delete'
    success_url = '/'
    # _delete
    # _confirm_Delete


class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    # 업데이트를 하고난 뒤 돌아갈 페이
    success_url = '/'
    # _update
    # _form


class BookmarkDetail(DetailView):
    model = Bookmark
    # _Detail
