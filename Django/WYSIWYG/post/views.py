from django.shortcuts import render


# Create your views here.
from django.views.generic.edit import CreateView
from .models import Post

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'post/create.html'