from django.contrib import admin
from .models import Category, Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Category)
admin.site.register(Photo,PhotoAdmin)
