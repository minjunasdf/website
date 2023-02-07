from django import forms
from .models import QnA


class QnaForm(forms.ModelForm):
    class Meta:
        model = QnA
        fields = ['subject', 'content']