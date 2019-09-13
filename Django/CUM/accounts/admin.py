from django.contrib import admin

# Register your models here.
from .models import User
from django.contrib.auth.admin import UserAdmin

# admin.site.register(User, UserAdmin)

class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets[1][1]['fields'] += ('profile', 'message')

    UserAdmin.add_fieldsets += (
        (('Additional Info'), {'fields': ('profile', 'message')}),
    )

admin.site.register(User, CustomUserAdmin)