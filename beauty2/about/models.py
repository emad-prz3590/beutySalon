from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class AboutUs(models.Model):
    title = models.CharField(max_length=200,verbose_name='عنوان')
    image = models.ImageField(upload_to='photos',verbose_name='تصویر',null=True)
    discription = RichTextUploadingField(verbose_name='متن درباره ما')
    
    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'
