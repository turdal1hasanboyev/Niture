# Generated by Django 4.2.14 on 2024-08-06 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='views',
        ),
    ]
