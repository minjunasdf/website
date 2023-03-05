from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainpage/main.html')


def permissionerror(request):
    return render(request, '403.html')