from django import forms
from textpage.models import Text, Comment


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['subject', 'content']
        labels = {
            'subject' : '글 제목',
            'content': '글 내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답변내용',
        }