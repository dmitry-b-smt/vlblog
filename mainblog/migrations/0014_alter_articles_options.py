# Generated by Django 3.2.4 on 2021-08-17 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0013_alter_articles_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
