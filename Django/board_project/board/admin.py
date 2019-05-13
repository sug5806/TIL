from django.contrib import admin

from .models import Category
from .models import Document


# Register your models here.


class CategoryOption(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', ]

    # name을 작성할때 자동으로 slug도 같이 작성됨
    prepopulated_fields = {'slug': ('name',)}


class DocumentOption(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'slug', 'created', 'updated', ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryOption)
admin.site.register(Document, DocumentOption)
