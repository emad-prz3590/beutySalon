from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver 
from ckeditor_uploader.fields import RichTextUploadingField
from django_jalali.db import models as jmodels
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'دسته بندی مقالات'
        verbose_name_plural = 'دسته بندی مقالات'


class Article(models.Model):
    title = models.CharField(verbose_name='عنوان',max_length=200)
    short_discription = models.TextField(verbose_name='توضیحات کوتاه',max_length=500,null=True)
    one_banner = models.ImageField(verbose_name='تصویر اول مقاله')
    two_banner = models.ImageField(verbose_name='تصویر دوم مقاله')
    tree_banner = models.ImageField(verbose_name='تصویر سوم مقاله')
    discription = RichTextUploadingField(verbose_name='متن مقاله')
    image = models.ImageField(verbose_name='تصویر شاخص',null=True)
    creation_date = jmodels.jDateField(auto_now_add=True,verbose_name='تاریخ_ایجاد')
    view = models.IntegerField(verbose_name='بازدید',default=0)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,verbose_name='دسته بندی')
    slug = models.SlugField(verbose_name='اسلاگ',blank=True,null=True,allow_unicode = True,help_text='یک اسلاگ معتبر متشکل از حروف، اعداد، زیرخط یا خط فاصله وارد کنید. ')

    meta_descreption = models.CharField(verbose_name='meta_Descreption',null=True,blank=True,max_length=500)
    meta_keyword = models.CharField(verbose_name='keyword',null=True,blank=True,max_length=500)
    meta_title = models.CharField(verbose_name='meta_title',null=True,blank=True,max_length=500)
    
    def __str__(self) -> str:
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
         
    


def unique_slug_generator(instance, new_slug=None):
    """
    This function generates a unique slug for instances of Article and Category models.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    # Check if the slug already exists in the database
    model_class = instance.__class__
    qs = model_class.objects.filter(slug=slug).exclude(pk=instance.pk)
    if qs.exists():
        # If the slug already exists, create a new slug with a random number appended
        new_slug = f"{slug}-{qs.count() + 1}"
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Article)
def article_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    This function generates a unique slug for Article instances before saving them.
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Category)
def category_pre_save_receiver(sender, instance, *args, **kwargs):
    """
    This function generates a unique slug for Category instances before saving them.
    """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        
