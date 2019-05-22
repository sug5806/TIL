from django.contrib import admin
from .models import User

# Register your models here.

from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('message', 'profile')}),
    )
    # UserAdmin.fieldsets[1][1]['fields']+=('profile','message')

    UserAdmin.add_fieldsets += (
        ('Additional Infoa', {'fields': ('message', 'profile')}),
    )

admin.site.register(User, CustomUserAdmin)

