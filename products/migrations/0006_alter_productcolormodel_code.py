# Generated by Django 4.0 on 2022-01-07 14:56

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productcolormodel_productsizemodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolormodel',
            name='code',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=10, samples=None, verbose_name='code'),
        ),
    ]