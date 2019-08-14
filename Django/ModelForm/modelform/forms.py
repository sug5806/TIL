from django import forms

from .models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        # 폼으로 사용하고 싶은 모델
        model = Product
        # 모델의 필드명을 적어줍니다
        fields = ['name', 'price', 'seller']
