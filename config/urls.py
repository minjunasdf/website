from django.contrib import admin
from django.urls import path, include
from textpage import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("textpage/", include('textpage.urls')),
    path("qna/", include('qna.urls')),
    path("", include('mainpage.urls')),
]