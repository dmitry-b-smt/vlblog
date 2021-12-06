# Generated by Django 3.2.4 on 2021-08-20 20:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0019_articles_innerimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='innerimg',
        ),
        migrations.AlterField(
            model_name='articles',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='article_img', verbose_name='Изображение статьи'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Основной текст статьи'),
        ),
    ]
