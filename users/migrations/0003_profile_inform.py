# Generated by Django 3.2.4 on 2021-08-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210722_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='inform',
            field=models.TextField(blank=True, null=True, verbose_name='Additional info'),
        ),
    ]
