# Generated by Django 2.2 on 2020-08-21 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vegetable', '0002_auto_20200809_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vegetable',
            name='price_per_kg',
        ),
    ]