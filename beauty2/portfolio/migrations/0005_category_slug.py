# Generated by Django 4.2 on 2023-05-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_category_options_alter_photo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, null=True, unique=True),
        ),
    ]
