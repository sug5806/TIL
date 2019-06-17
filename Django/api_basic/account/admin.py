from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdminOption(UserAdmin):
    UserAdmin.fieldsets[1][1]['fields'] += ('message', 'profile')

    UserAdmin.add_fieldsets += (
        (('Additional Info'), {'fields': ('message', 'profile')}),
    )

admin.site.register(User, UserAdminOption)