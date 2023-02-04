from django.shortcuts import render, get_object_or_404
from .models import Text


def index(request):
    text_list = Text.objects.order_by('id')
    content = {'text_list' : text_list}

    return render(request, 'textpage/textpage_list.html', content)

def detail(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    content = {'text' : text}
    return render(request, 'textpage/text_detail.html', content)