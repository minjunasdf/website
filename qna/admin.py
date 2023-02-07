from django.contrib import admin
from .models import QnA

class Search_Text_Admin(admin.ModelAdmin):
    search_fields = ['subject','content']

admin.site.register(QnA, Search_Text_Admin)