from django.contrib import admin
from .models import User
from pprint import pprint

# Register your models here.

from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):

    # fieldsets : 유저의 상세정보를 볼때 커스텀 필드를 추가 시킴
    # 맨 마지막에 필드를 만들어 추가시킴
    # fieldsets = UserAdmin.fieldsets + (
    #     ('Additional Info', {'fields': ('message', 'profile')}),
    # )

    # 기존에 있는 필드에 추가를 시킨다
    UserAdmin.fieldsets[3][1]['fields'] += ('profile', 'message')


    # add_fieldsets : 유저를 만들때 커스텀 필드를 추가시킴
    UserAdmin.add_fieldsets += (
        ('Additional Info', {'fields': ('message', 'profile')}),
    )

admin.site.register(User, CustomUserAdmin)

