import math

# 로그인을 하지 않으면 글쓰기 불가
from django.contrib.auth.decorators import login_required

# Filter를
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
from .models import Category
from .models import Board


# QuerySet은 모델의 디폴트 매니저를 통해 실행한다.
# Create your views here.

def search_list(request):
    # page = int(request.GET.get('page', 1))
    # paginated_by = 5

    # cb_list = request.GET.getlist('cb', None)
    search_key = request.GET.get('search_key', None)
    # search_key = key
    if not search_key:
        # search_type = None, search_type = []
        search_key = ''

    if search_key:
        document_p = Q(text__icontains=search_key)
        category_and_board_p = Q(name__icontains=search_key)

        # print(get_list_or_404(Board, category_and_board_p, None))

        documents = Document.objects.filter(document_p)
        categorys = Category.objects.filter(category_and_board_p)
        boards = Board.objects.filter(category_and_board_p)

        documents = get_list_or_404(Document, document_p) if documents else None
        categorys = get_list_or_404(Category, category_and_board_p) if categorys else None
        boards = get_list_or_404(Board, category_and_board_p) if boards else None

    else:
        documents = get_list_or_404(Document)
        categorys = get_list_or_404(Category)
        boards = get_list_or_404(Board)

    # total_count = len(documents)
    # start_index = paginated_by * (page - 1)
    # end_index = paginated_by * page
    # documents = documents[start_index:end_index]

    return render(request, 'board/search_list.html',
                  {'document_list': documents, 'board_list':boards, 'category_list' : categorys, })


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
    # search_key = request.GET.get('search_key', None)
    # if not search_key:
    #     # search_type = None, search_type = []
    #     search_type = ['text']
    # search_q = None

    """
    과제 1 : Document, Category, Board 모델까지 확장
    Category - Board = models.ForeignKey(Board)
    * 게시판 : Category - 질문, 답변, 판매, 구매
    * 쇼핑몰 : Category - 상위 카테고리 - 상의 -하위 카테고리, 하의
            - Category에 depth를 어떻게 구현할 것이냐?
            
    과제 2 : 검색 페이지 구현, Board?, Category?, Document?
    Ex) Programming 이라는 이름을 가진 게시판?
    Programming 이라는 이름을 가진 카테고리?
    Programming 이라는 내용이 들어간 게시글이 있느냐?
    
    과제 3 : 전화번호부 구현 - 이름, 전화번호, 메모 
    
    """

    # if search_key and cb_list:
    #     if 'title' in cb_list:
    #         temp_p = Q(title__icontains=search_key)
    #         search_q = search_q | temp_p if search_q else temp_p
    #     if 'text' in cb_list:
    #         temp_p = Q(text__icontains=search_key)
    #         search_q = search_q | temp_p if search_q else temp_p
    #     if 'author' in cb_list:
    #         temp_p = Q(author__username__icontains=search_key)
    #         search_q = search_q | temp_p if search_q else temp_p
    #
    #     documents = get_list_or_404(Document, search_q)
    #
    # else:
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


    # html = render_to_string('board/document_list.html', {'object_list':documents, 'range': range(1, math.ceil(total_count / paginated_by) + 1)})
    # return JsonResponse({'html': html})

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




    """
    2019-05-15 수업
    from django.db.models import F
    Document.objects.filter(text__icontains='11')
    
    F : 컬럼 참조
    Join
    select_related -> DB에 부담을 줄 것이냐? 아니면 서버에 부담을 줄것이냐?
    Document.objects.select_related('author').all()
    1)select_related -> Join Query를 만들어서 한큐에 데이터를 불러온다.
        * ForeingnKey까지만 묶을 수 있다.
    2) prefetch_related -> Join을 사용하지 않음
        * Document를 부르고, Category를 부러서 코드 단에서 병합한다.
        * ManyToMany 이런것도 지원함
        * selete_related로 할수 없는 것은 prefetch_related를 사용한다.
        
    
    author를 가져오는데 inner_join을 통해 DB access를 줄인다.
    inner_join : 서로 가지고 있는 데이터만 합쳐서 보여준다 -> 교집합
    outer_join : 서로 가지고 있는 데이터와 함께 어떤 테이블을 기준으로 레코드를 가져오는데 없으면 null로 가져온다
    
    Document.objects.prefetch_related('author').all()
    
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

    # GET일 경우
    else:
        # 입력 창을 보여줌
        form = DocumentForm()
    return render(request, 'board/document_create.html', {'form': form})




@receiver(pre_save, sender=Document)
def pre_save(sender, instance, **kwargs):
    # create할때 슬러그를 적지않으니 공백으로 입력되어
    # 중복으로 인해 생성이 안된다 그리하여 slug를 sugify를 통해 title과 같게 만든다
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
        form = DocumentForm(instance=Document.objects.get(pk=document_id))
        # form = get_object_or_404(Document, pk=document_id)
    return render(request, 'board/document_update.html', {'form': form})


from .forms import CommentForm
from django.template.loader import render_to_string
# Todo 댓글기능 따로 만들기
def comment_create(request, document_id):
    # ajax 기능에 의해 호출된 것인지 구분하기 위한 값
    is_ajax = request.POST.get('is_ajax')

    document = get_object_or_404(Document, pk=document_id)
    comment_form = CommentForm(request.POST)
    comment_form.instance.author_id = request.user.id
    comment_form.instance.document_id = document_id
    if comment_form.is_valid():
       comment = comment_form.save()

    # 만약 ajax에 의해 호출되었다면 redirection없이 Json 형태로 응답
    if is_ajax:
        ## 데이터를 만들어서 던져준다
        # html = """
        # <tr>
        #     <td colspan="3">{}</td>
        #     <td>{}</td>
        #     <td>{}</td>
        #     <td><a href="{}" class="btn btn-warning btn-sm">update</a></td>
        #     <td><a href="{}" class="btn btn-danger btn-sm">delete</a></td>
        # </tr>
        # """.format(comment.text, comment.author.username, comment.created, "url1", "url2")
        html = render_to_string('board/comment_single.html', {'comment': comment})
        return JsonResponse({'html': html})

    return redirect(document)
    # return redirect(reverse('board:detail', args=[document_id]))


"""
함수형 뷰
페이지에 접근했을때 구동되는 로직들
1) 해당 객체가 있는지 확인 - get_object_or_404, objects.get, objects.filter.exists
2) 객체에 대한 권한 체크 - 작성자, 관리자
3-1) get -> 해당 페이지에 필요한 값 입력받기
3-2) post -> 입력받은 값에 대한 처리 -> 삭제, 업데이트
4) 처리 후 페이지 이동



클래스형 뷰
페이지에 접근했을때 구동되는 로직들
def dispatch(self, request, *args, **kwargs):
    object = self.get-object()
    # 권한 체크
    # super().dispatch(request, *agrs, **kwargs) -이것만 사용하던가 이걸 사용하지 않으면 밑의 if문 사용
    if request.method == "POST":
        # super().post(request, *args, **kwargs) 
    else:
        # super().get(request, *args, **kawags)
## 함수형 뷰와 로직순서는 똑같으나 dispatch에서 확인하기 때문에 순서를 바꾼것 뿐이다
1) 객체에 대한 권한 체크 - 작성자, 관리자 - dispatch
2) 해당 객체가 있는지 확인 - get_object, get_queryset
3-1) get -> 해당 페이지에 필요한 값 입력받기 - def get
3-2) post -> 입력받은 값에 대한 처리 -> 삭제, 업데이트 - def post
4) 처리 후 페이지 이동

"""

from django.contrib import messages
from .models import Comment

def comment_update(request, comment_id):
    is_ajax, data = (request.POST.get('is_ajax'), request.GET) if 'is_ajax' in request.GET else (request.POST.get('is_ajax', False), request.POST)

    # Comment모델에서 comment_id에 해당하는 레코드를 전부 가져온다
    comment = get_object_or_404(Comment, pk=comment_id)

    # Document 모델에서
    document = get_object_or_404(Document, pk=comment.document.id)

    if request.user != comment.author:
        messages.warning(request, "권한 없음")
        return redirect(document)

    if is_ajax:
        form = CommentForm(data, instance=comment)
        if form.is_valid():
            form.save()
            return JsonResponse({'works': True})


    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(document)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'board/comment_update.html', {'form': form})



###################################################################################

def comment_delete(request, comment_id):

    is_ajax = request.POST.get('is_ajax')

    comment = get_object_or_404(Comment, pk=comment_id)
    document = get_object_or_404(Document, pk=comment.document.id)

# user.is_staff
# user.is_superuser

    if request.user != comment.author and not request.user.is_staff and request.user != document.author:
        messages.warning(request, "권한 없음")
        return redirect(document)

    if is_ajax:
        comment.delete()
        return JsonResponse({"works": True})

    if request.method == "POST":
        comment.delete()
        return redirect(document)
    else:
        return render(request, 'board/comment_delete.html', {'object':comment})


def document_detail(request, document_id):
    # 레코드 1개 가져오기
    # document_id를 하면 없다고 뜨니 매개변수로 document_id를 받는다
    # urls 파일에 가서 document_id를 넘겨준다
    #document = Document.objects.get(pk=document_id)
    document = get_object_or_404(Document, pk=document_id)

    # 만약 post일 때만 댓글 입력에 관한 처리를 더한다.
    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST)
    #     comment_form.instance.author_id = request.user.id
    #     comment_form.instance.document_id = document_id
    #     if comment_form.is_valid():
    #         comment_form.save()

    comment_form = CommentForm()
    # 2019-05-16 Todo 해당 document(글)에 대해 달린 댓글을 모두 가져온다
    comments = document.comments.all()
    return render(request, 'board/document_detail.html',
                  {
                      'object': document,
                      'comments' : comments,
                      'comment_form' : comment_form,
                  }
                  )

def document_delete(request, document_id):
    # 객체 불러와서 delete를 호출
    # Document.objects.get(pk=document_id).delete()
    get_object_or_404(Document, pk=document_id).delete()
    return render(request, 'board/document_delete.html')

    # 과제 1 : delete_View 구현하기
    # 내일 하는것 : get_object_or_404, get_list_or_404, paging

    # 과제 2 : bootstrap 적용해오기

########################
# filter(field 이름) : 매칭
# filter(field 이름__옵션) : 옵션으로 매칭
# Document.objects.filter(pk=25, title=?)을 하면 and로 한다 Ex) pk=25이고 title이 ?인것

from allauth.account.signals import user_signed_up
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver

# 시그널이 발생했을 때 발생하는 실행될 함수
@receiver(user_signed_up)
def naver_signup(request, user, **kwargs):
    social_user = SocialAccount.objects.filter(user=user)
    if social_user.exists():
        user.last_name = social_user[0].extra_data['name']
        user.save()
# 시그널과 해당 함수를 connect
# 시그널 연결 방법 2가지 receiver 쓰는 방법, connect 쓰는방법
# user_signed_up.connect(naver_signup)



# Todo 2019-05-17 금요일 수업
"""
일번적인 경우 데이터를 전송하기 위해 JSON형태로 전송
dictionary 형태로 온다고 생각하면 된다
"""
from django.http import JsonResponse
def get_data_ajax(request):
    data = {
        "name": 'Jake',
        "age": 100,
        "bloodtype": "O",
    }
    return JsonResponse(data)

def get_data_list(request):
    page = int(request.GET.get('page', 1))
    paginated_by = 5
    documents = get_list_or_404(Document)

    total_count = len(documents)
    start_index = paginated_by * (page - 1)
    end_index = paginated_by * page
    documents = documents[start_index:end_index]

    html = render_to_string('board/document_list.html',
                            {'object_list': documents,
                             'range': range(1, math.ceil(total_count / paginated_by) + 1),
                             }
                            )
    return JsonResponse({'html' : html}, )