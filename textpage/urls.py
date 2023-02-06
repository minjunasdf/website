from django.urls import path
from . import views

app_name = 'textpage'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:text_id>/', views.detail, name='detail'),
    path('comment/create/<int:text_id>/', views.comment_create, name='comment_create'),
    path('text/create/', views.text_create, name='text_create'),
]