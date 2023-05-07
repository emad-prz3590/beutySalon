from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget




class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    formfield_overrides = {
        models.TextField: { 'widget' : CKEditorUploadingWidget},
    }

    class Media:
        js = ('https://cdn.ckeditor.com/4.16.1/full-all/ckeditor.js', 'https://cdn.ckeditor.com/4.16.1/full-all/adapters/jquery.js')

    

admin.site.register(AboutUs,AboutUsAdmin)
