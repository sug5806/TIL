from django.contrib import admin

from .models import Category
from .models import Document
from .models import Board
from .models import Comment


# Register your models here.

class BoardOption(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Board, BoardOption)

class CategoryOption(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'board', ]

    # name을 작성할때 자동으로 slug도 같이 작성됨
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryOption)

class CommentInline(admin.TabularInline):
    model = Comment



class DocumentOption(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'slug', 'created', 'updated', 'category', 'board', ]
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]

admin.site.register(Document, DocumentOption)






admin.site.register(Comment)
