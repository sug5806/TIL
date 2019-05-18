from django import forms

from .models import Document
from .models import Comment


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document

        fields = ['category', 'title', 'text', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = "댓글"

