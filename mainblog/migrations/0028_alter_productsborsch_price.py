# Generated by Django 3.2.4 on 2021-10-06 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0027_productsborsch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsborsch',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Стоимость продукта за кг'),
        ),
    ]
