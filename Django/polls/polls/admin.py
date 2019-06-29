from django.contrib import admin

from .models import *


# Register your models here.

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'votes', ]
    list_display_links = ['question', ]
    list_editable = ['votes', 'choice_text']


admin.site.register(Choice, ChoiceAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', ]


admin.site.register(Question, QuestionAdmin)
