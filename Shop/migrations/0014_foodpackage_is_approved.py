# Generated by Django 2.2 on 2020-07-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0013_auto_20200709_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodpackage',
            name='is_approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]