from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'view')
    search_fields = ('title', 'content')
    list_filter = ('creation_date',)
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article, ArticleAdmin)