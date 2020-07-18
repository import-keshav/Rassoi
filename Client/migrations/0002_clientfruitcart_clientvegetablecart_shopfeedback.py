# Generated by Django 2.2 on 2020-07-18 11:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0019_auto_20200718_1108'),
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopFeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('number_of_stars', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_shop_feedback_client', to='Client.Client')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_shop_feedback_shop', to='Shop.Shop')),
            ],
            options={
                'verbose_name': 'Shop FeedBack',
                'verbose_name_plural': 'Shop FeedBacks',
            },
        ),
        migrations.CreateModel(
            name='ClientVegetableCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_items', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_client_vegetable_cart_client', to='Client.Client')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_client_vegetable_cart_shop', to='Shop.Shop')),
                ('vegetable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_client_vegetable_cart_vegetable', to='Shop.Vegetable')),
            ],
            options={
                'verbose_name': 'Client Vegetable Cart',
                'verbose_name_plural': 'Client Vegetable Carts',
            },
        ),
        migrations.CreateModel(
            name='ClientFruitCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_items', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_client_fruit_cart_client', to='Client.Client')),
                ('fruit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_client_fruit_cart_fruit', to='Shop.Fruit')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_client_fruit_cart_shop', to='Shop.Shop')),
            ],
            options={
                'verbose_name': 'Client Fruit Cart',
                'verbose_name_plural': 'Client Fruit Carts',
            },
        ),
    ]