# Generated by Django 4.0 on 2022-01-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productcolormodel_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolormodel',
            name='code',
            field=models.CharField(max_length=10, verbose_name='code'),
        ),
    ]
