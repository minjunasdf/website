from django.shortcuts import render, get_object_or_404, redirect
from .models import Text, Comment
from django.utils import timezone
from .forms import TextForm


def index(request):
    text_list = Text.objects.order_by('id')
    content = {'text_list' : text_list}

    return render(request, 'textpage/textpage_list.html', content)

def detail(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    content = {'text' : text}
    return render(request, 'textpage/text_detail.html', content)

def comment_create(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    comment = Comment(texts = text, content=request.POST.get('content'), create_date=timezone.now())
    comment.save()
    return redirect('website:detail', text_id=text.id)

def text_create(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.create_date = timezone.now()
            t.save()
            return redirect('website:index')
    else:
         form = TextForm()
    context = {'form':form}
    return render(request, 'textpage/text_form.html', context)