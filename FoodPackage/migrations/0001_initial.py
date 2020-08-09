# Generated by Django 2.2 on 2020-08-09 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0002_auto_20200807_0241'),
        ('Shop', '0002_auto_20200807_0244'),
        ('Food', '0002_auto_20200809_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_package_food_package_client', to='Client.Client')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_package_food_package_shop', to='Shop.Shop')),
            ],
            options={
                'verbose_name': 'Food Package',
                'verbose_name_plural': 'Food Packages',
            },
        ),
        migrations.CreateModel(
            name='FoodPackageMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('food_package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_package_food_package_meals_food_package', to='FoodPackage.FoodPackage')),
                ('meal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_package_food_package_meals_meal', to='Food.FoodMeal')),
            ],
            options={
                'verbose_name': 'Food Package Meal',
                'verbose_name_plural': 'Food Package Meal',
            },
        ),
    ]
