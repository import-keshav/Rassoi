# Generated by Django 2.2 on 2020-09-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0003_remove_foodmeal_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmeal',
            name='day',
            field=models.TextField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], null=True),
        ),
    ]
