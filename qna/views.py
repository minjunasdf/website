from django.shortcuts import render, get_object_or_404, redirect
from .models import QnA
from django.utils import timezone
from .forms import QnaForm

def index(request):
    text_list = QnA.objects.order_by('-create_date')
    content = {'text_list' : text_list}

    return render(request, 'qna/qna_list.html', content)

def qna_create(request):
    if request.method == 'POST':
        form = QnaForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.create_date = timezone.now()
            t.save()
            return redirect('qna:index')
    else:
         form = QnaForm()
    context = {'form':form}
    return render(request, 'qna/qna_form.html', context)