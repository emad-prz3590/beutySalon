from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='عنوان')
    slug = models.SlugField(unique=True,allow_unicode=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'دسته بندی نمونه کار ها'
        verbose_name_plural = 'دسته بندی نمونه کار ها'
    
class Photo(models.Model):
    title = models.CharField(max_length=200,verbose_name='عنوان')
    image = models.ImageField(upload_to='photos' , verbose_name='تصویر')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کار'