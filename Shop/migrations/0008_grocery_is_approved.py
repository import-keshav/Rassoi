# Generated by Django 2.2 on 2020-07-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_auto_20200702_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocery',
            name='is_approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]