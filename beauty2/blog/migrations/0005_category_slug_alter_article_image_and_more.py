# Generated by Django 4.2 on 2023-05-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_banner_article_discription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='تصویر شاخص'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
