from django.db import models


# Create your models here.

from ckeditor_uploader.fields import RichTextUploadingField
class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='sub_categories')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True)
    image = models.ImageField(upload_to='product_images/%Y/%m/%d')
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    available_display = models.BooleanField(default=True)
    available_order = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return "["+ self.category.name+']' + self.name
