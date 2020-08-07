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
            name='Grocery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('is_available', models.BooleanField(blank=True, default=True, null=True)),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grocery_grocery_shop', to='Shop.Shop')),
            ],
            options={
                'verbose_name': 'Grocery',
                'verbose_name_plural': 'Groceries',
            },
        ),
        migrations.CreateModel(
            name='GroceryPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('amount', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('price_type', models.TextField(blank=True, choices=[('KG', 'KG'), ('Lts', 'Lts'), ('No', 'No')], null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('grocery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_grocery_price_grocery', to='Grocery.Grocery')),
            ],
            options={
                'verbose_name': 'Grocery Price',
                'verbose_name_plural': 'Grocery Price',
            },
        ),
    ]