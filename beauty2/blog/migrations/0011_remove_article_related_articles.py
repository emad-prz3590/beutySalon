# Generated by Django 4.2 on 2023-05-03 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_related_articles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='related_articles',
        ),
    ]
