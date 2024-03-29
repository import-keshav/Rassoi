# Generated by Django 2.2 on 2020-08-07 02:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('price_per_kg', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('is_available', models.BooleanField(blank=True, default=False, null=True)),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vegetable_vegetable_shop', to='Shop.Shop')),
            ],
            options={
                'verbose_name': 'Vegetable',
                'verbose_name_plural': 'Vegetables',
            },
        ),
        migrations.CreateModel(
            name='VegetablePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('amount', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('price_type', models.TextField(blank=True, choices=[('KG', 'KG')], null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('vegetable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vegetable_vegetable_price_vegetable', to='Vegetable.Vegetable')),
            ],
            options={
                'verbose_name': 'Vegetable Price',
                'verbose_name_plural': 'Vegetable Price',
            },
        ),
    ]
