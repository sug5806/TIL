from django import template
from django.template.loader import render_to_string

register = template.Library()

# 커스텀 템플릿 필터 정의
@register.filter
def add_two(value):
    return value + 2


# 커스텀 템플릿 태그 정의
@register.simple_tag
def print_template():
    return render_to_string('example/test.html')


# 추가 인자가 있는 필터 정의
@register.filter
def string_append(left, right):
    return left+"-"+right

