# Generated by Django 2.2 on 2020-08-07 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='location_coordinates',
            new_name='latitude',
        ),
        migrations.AddField(
            model_name='client',
            name='longitude',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
