from django.shortcuts import render, get_object_or_404, redirect
from .models import Text, Comment
from django.utils import timezone
from .forms import TextForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator

def comment_group_check(user):
    return "comment_allow" in user.groups.all()

def texts_group_check(user):
    return "texts_allow" in user.groups.all()

def index(request):
    page = request.GET.get('page', '1')
    text_list = Text.objects.order_by('-create_date')
    paginator = Paginator(text_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    content = {'text_list': page_obj}
    return render(request, 'textpage/textpage_list.html', content)

def detail(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    content = {'text' : text}
    return render(request, 'textpage/text_detail.html', content)

@login_required(login_url='common:login')
def comment_create(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.texts = text
            answer.author = request.user
            answer.save()
            return redirect('textpage:detail', text_id=text.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'text': text, 'form': form}
    return render(request, 'textpage/text_detail.html', context)

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