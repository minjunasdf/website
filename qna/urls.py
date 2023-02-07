from django.urls import path
from . import views

app_name = 'qna'

urlpatterns = [
    path('', views.index, name='index'),
    path('qna/create/', views.qna_create, name='qna_create'),
]