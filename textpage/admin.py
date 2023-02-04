from django.contrib import admin
from .models import Text, Comment


class Search_Text_Admin(admin.ModelAdmin):
    search_fields = ['subject','content']

class Search_Comment_Admin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Text, Search_Text_Admin)
admin.site.register(Comment, Search_Comment_Admin)