# Generated by Django 2.2 on 2020-08-07 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_free', models.BooleanField(blank=True, default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('shop_assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_driver_shop', to='Shop.Shop')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_driver_user', to='User.User')),
            ],
            options={
                'verbose_name': 'Driver',
                'verbose_name_plural': 'Drivers',
            },
        ),
        migrations.CreateModel(
            name='DriverNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('notification_text', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_driver_notification_client', to='Driver.Driver')),
            ],
            options={
                'verbose_name': 'Driver Notification',
                'verbose_name_plural': 'Driver Notifications',
            },
        ),
    ]
