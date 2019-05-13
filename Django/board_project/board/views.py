from django.shortcuts import render

from .models import Document


# QuerySet은 모델의 디폴트 매니저를 통해 실행한다.
# Create your views here.


def document_list(request):
    # QuerySet
    # 1. 객체를 선택
    # 2. 객체 생성
    # 3. 객체 필터링
    # 4. 객체 삭제

    # 1. 모델의 전체 데이터 불러오기
    # objects는 모델의 manager를 의미한다
    documents = Document.objects.all()

    return render(request, 'board/document_list.html', {'object_list': documents})


from .forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse


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
            document = form.save()
            # reverse : 이름을 기준으로 url을 만들어준다.
            return redirect(reverse('board:detail', args=[document.id]))

    else:
        # 입력 창을 보여줌
        form = DocumentForm()
    return render(request, 'board/document_create.html', {'form': form})


def document_update(request, document_id):
    # 객체 불러와서 데이터를 수정한다
    # form = DocumentForm(request.POST, request.FILES)

    # 수정을 하려고했으나 slug exists가 뜨니 수정이 아닌 새로 생성해서 넣는것이 된다
    if request.method == "POST":
        document = Document.objects.get(pk=document_id)
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


    return render(request, 'board/document_update.html', {'form': form})


def document_detail(request, document_id):
    # 레코드 1개 가져오기
    # document_id를 하면 없다고 뜨니 매개변수로 document_id를 받는다
    # urls 파일에 가서 document_id를 넘겨준
    document = Document.objects.get(pk=document_id)
    return render(request, 'board/document_detail.html',
                  {'object': document})


def document_delete(request, document_id):
    # 객체 불러와서 delete를 호출
    Document.objects.get(pk=document_id).delete()
    return render(request, 'board/document_delete.html')

    # 과제 1 : delete_View 구현하기
    # 내일 하는것 : get_object_or_404, get_list_or_404, paging

    # 과제 2 : bootstrap 적용해오기