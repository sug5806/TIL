from django.contrib import admin
from .models import AdminPage
# Register your models here.


class AdminPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'address']
    search_fields = ['name']
    # 수정 하고자하는 필드 이름을 적어줍니다.
    list_editable = ['age', 'address']
    # 클릭하고 싶은 필드를 적어줍니다.
    list_display_links = ['id', 'name']


admin.site.register(AdminPage, AdminPageAdmin)