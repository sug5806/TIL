import math

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify

from .forms import DocumentForm
from .models import Document


# QuerySet은 모델의 디폴트 매니저를 통해 실행한다.
# Create your views here.


def document_list(request):
    # QuerySet
    # 1. 객체를 선택
    # 2. 객체 생성
    # 3. 객체 필터링
    # 4. 객체 삭제

    # 현재 페이지 번호
    page = int(request.GET.get('page', 1))
    # 페이징 기능을 구현한다.
    # 페이지당 갯수
    paginated_by = 5

    ##############################################################################

    # 체크박스 값 가져오기
    # request.METHOD.get -> 아이템 1개
    # request.METHOD.getlist -> 리스트 형태로
    cb_list = request.GET.getlist('cb', None)

    """
    username => Q(author__username__icontains=search_key)
    title => Q(title__icontains=search_key)
    text => Q(text__icontains=search_key)
    """

    # 검색어 가져오기
    search_key = request.GET.get('search_key', None)
    search_q = None

    """
    과제 1 : Document, Category, Board 모델까지 확장
    과제 2 : 검색 페이지 구현, Board?, Category?, Document?
    과제 3 : 전화번호부 구현 - 이름, 전화번호, 메모 
    """

    if search_key and cb_list:
        if 'title' in cb_list:
            temp_p = Q(title__icontains=search_key)
            search_q = search_q | temp_p if search_q else temp_p
        if 'text' in cb_list:
            temp_p = Q(text__icontains=search_key)
            search_q = search_q | temp_p if search_q else temp_p
        if 'author' in cb_list:
            temp_p = Q(author__username__icontains=search_key)
            search_q = search_q | temp_p if search_q else temp_p

        documents = get_list_or_404(Document, search_q)

    else:
        documents = get_list_or_404(Document)

    ##############################################################################

    # 1. 모델의 전체 데이터 불러오기
    # objects는 모델의 manager를 의미한다
    # documents = Document.objects.all()
    # documents = Document.objects.filter(title__contains='1')

    # objets.all을 get_list_or_404가 해준다
    # documents = get_list_or_404(Document)
    # documents = get_list_or_404(Document, title__icontains='검색어')

    # QuerySet 객체를 슬라이싱 할 떄 [시작:끝]
    # 1 - 0 ======== page*pagenated_by
    # 2 - paginated_by*(page-1) ======= 6
    # 3 - paginated_by*(page-1) ======= 9

    # 전체 갯수 -> 전체 페이지수
    total_count = len(documents)
    start_index = paginated_by * (page - 1)
    end_index = paginated_by * page
    documents = documents[start_index:end_index]

    """
    필드명 = "값" 매칭
    필드명__exact = "값" 매칭
    필드명__iexact = "값" 대소문자 구분없이 매칭
    
    __startswith, __istartwith 값으로 시작
    __endswith, __iendswith 값으로 끝
    __contains, __icontains 값을 포함하느냐
    
    ForeignKey 매칭
    필드명__해당모델의필드명 매칭
    필드명__해당모델의플드명__옵션 : 위와 동일하게 동작
    
    __gt=값, __gte=값 : 크다, 크거나 같다.
    ex) created__gt = 오늘 : 작성일이 오늘보다 이후다
    __lt=값, __lte=값 : 작다, 작거나 같다.
    ex) created_lt = 오늘 : 작성일이 오늘보다 이전이다
    ex) 판매시작일__lte = 오늘 : 판매시작일 설정값이 오늘보다 이전이거나 같으면 판매 시작
    """

    """
    objects.filter() : filter 메서드에 들어가는 매개변수들은 항상 and연산을 한다.
    or 연산을 하고 싶어서 Q 객체를 사용한다.
    사용법은 filter에 들어가는 매개변수의 작성법과 똑같다.
    
    Q() | Q() : or
    Q() & Q() : and
    ~Q() : not
    """

    return render(request, 'board/document_list.html',
                  {'object_list': documents, 'range': range(1, math.ceil(total_count / paginated_by) + 1)})


# 로그인한 사용자만 글쓰기가 가능하다
@login_required
def document_create(request):
    # Document.objects.create()로 만든다 -> 실행과 동시에 DB에 삽입된다
    # 분기 - post, get
    if request.method == 'POST':
        # 처리를 해야함
        # 입력받은 데이터를 request.POST로 가져온다
        # request.POST : 폼에서 입력한 텍스트 데이터
        # request.FILES : 폼에서 입력한 파일 데이터
        # 서버로 보낼때 텍스트 데이터와 파일 데이터는 따로 보낸
        # 제네릭 뷰에서는 따로 처리를 하지 않는다?
        form = DocumentForm(request.POST, request.FILES)
        # 작성자필드 author_id를 로그인한 사용자의 id로 정한다
        form.instance.author_id = request.user.id
        if form.is_valid():
            # form.instance.slug = slugify(form.instance.title)
            document = form.save()
            # reverse : 이름을 기준으로 url을 만들어준다.
            return redirect(reverse('board:detail', args=[document.id]))

    else:
        # 입력 창을 보여줌
        form = DocumentForm()
    return render(request, 'board/document_create.html', {'form': form})

# create할때 슬러그를 적지않으니 공백으로 입력되어
# 중복으로 인해 생성이 안된다 그리하여 slug를 sugify를 통해 title과 같게 만든다
@receiver(pre_save, sender=Document)
def pre_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)


def document_update(request, document_id):
    # 객체 불러와서 데이터를 수정한다
    # form = DocumentForm(request.POST, request.FILES)

    # 수정을 하려고했으나 slug exists가 뜨니 수정이 아닌 새로 생성해서 넣는것이 된다
    if request.method == "POST":
        # document = Document.objects.get(pk=document_id)
        document = get_object_or_404(pk=document_id)
        # 모델폼을 사용할 때 instance를 넘겨주면, 해당 인스턴스값으로 초기화가 되고
        # 만약 pk가 있는 instance라면 update를 수행한다.
        # request.POST와 instance가 같이 전달되면, POST 데이터가 우선순위가 더 높다 = POST 데이터로 덮어쓸 수 있다

        # instance를 해서 id까지 가져오기 때문에 id를 포함한 전 필드로? 구분되기 떄문에 중복이 아니라 뜬다
        form = DocumentForm(request.POST, request.FILES, instance=document)

        if form.is_valid():
            # 저장이되고 해당 인스턴스가 반환된다
            document = form.save()
            return redirect(reverse('board:detail', args=[document.id]))
    else:
        # instance를 통해 객체를
        # form = DocumentForm(instance=Document.objects.get(pk=document_id))
        form = get_object_or_404(Document, pk=document_id)
    return render(request, 'board/document_update.html', {'form': form})


def document_detail(request, document_id):
    # 레코드 1개 가져오기
    # document_id를 하면 없다고 뜨니 매개변수로 document_id를 받는다
    # urls 파일에 가서 document_id를 넘겨준
    # document = Document.objects.get(pk=document_id)
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'board/document_detail.html',
                  {'object': document})


def document_delete(request, document_id):
    # 객체 불러와서 delete를 호출
    # Document.objects.get(pk=document_id).delete()
    get_object_or_404(Document, pk=document_id).delete()
    return render(request, 'board/document_delete.html')

    # 과제 1 : delete_View 구현하기
    # 내일 하는것 : get_object_or_404, get_list_or_404, paging

    # 과제 2 : bootstrap 적용해오기

#######
# filter(field 이름) : 매칭
# filter(field 이름__옵션) : 옵션으로 매칭
# Document.objects.filter(pk=25, title=?)을 하면 and로 한다 Ex) pk=25이고 title이 ?인것
