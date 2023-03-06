from django.urls import path
from . import views

app_name = 'textpage'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:text_id>/', views.detail, name='detail'),
    path('comment/create/<int:text_id>/', views.comment_create, name='comment_create'),
    path('text/goodvote/<int:text_id>/', views.text_goodvote, name='text_goodvote'),
path('text/badvote/<int:text_id>/', views.text_badvote, name='text_badvote'),
    path('text/create/', views.text_create, name='text_create'),
]