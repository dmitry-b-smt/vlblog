# Generated by Django 3.2.4 on 2021-07-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0006_rename_name_comments_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Автор комментария'),
        ),
    ]
