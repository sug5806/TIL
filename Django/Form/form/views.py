from django.shortcuts import render, redirect

from form.models import Product
from .forms import ProductForm


# Create your views here.

def list_create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/')

    objects_list = Product.objects.all()
    context = {
        'objects_list': objects_list,
        'form': form,
    }
    return render(request, template_name='form/product_list_create.html', context=context)
