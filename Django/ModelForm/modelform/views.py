from django.shortcuts import render, redirect

from .models import Product
from .forms import ProductModelForm


# Create your views here.

def list_create_product(request):
    # 먼저 빈 폼을 만들어 줍니다
    form = ProductModelForm()
    # 등록 버튼을 누른 요청이면
    if request.method == "POST":
        # 입력 정보를 기반으로 폼을 채웁니다
        form = ProductModelForm(request.POST)
        # 입력 정보가 유효 하다면
        if form.is_valid():
            # form.save 명령어를 통해 데이터를 저장합니다.
            form.save()
            # 생성이 완료되면 홈으로 돌아갑니다
            return redirect('/')
    # POST 요청이 아니면
    # Product의 모든 데이터를 가져옵니다
    objects_list = Product.objects.all()
    # context 변수에 담아줍니다.
    context = {
        'objects_list': objects_list,
        'form': form,
    }
    # product_list_create.html로 렌더링을 합니다
    return render(request, template_name='form/product_list_create.html', context=context)