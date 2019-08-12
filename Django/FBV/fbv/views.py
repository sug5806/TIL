from django.shortcuts import render


# Create your views here.

def fbv_post(request):
    if request.method == "GET":
        return render(request, template_name='fbv/index.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        print(request)
        print(request.POST)
        context = {
            'name': name,
        }
        return render(request, template_name='fbv/index.html', context=context)
