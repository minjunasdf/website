from django.shortcuts import render, get_object_or_404, redirect
from .models import Text, Comment
from django.utils import timezone
from .forms import TextForm
from django.contrib.auth.decorators import login_required


def index(request):
    text_list = Text.objects.order_by('-create_date')
    content = {'text_list' : text_list}

    return render(request, 'textpage/textpage_list.html', content)

def detail(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    content = {'text' : text}
    return render(request, 'textpage/text_detail.html', content)

@login_required(login_url='common:login')
def comment_create(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    comment = Comment(texts = text, content=request.POST.get('content'), create_date=timezone.now(), author=request.user)
    comment.save()
    return redirect('textpage:detail', text_id=text.id)

@login_required(login_url='common:login')
def text_create(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.author = request.user
            t.create_date = timezone.now()
            t.save()
            return redirect('textpage:index')
    else:
         form = TextForm()
    context = {'form':form}
    return render(request, 'textpage/text_form.html', context)