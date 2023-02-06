from django import forms
from textpage.models import Text


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['subject', 'content']