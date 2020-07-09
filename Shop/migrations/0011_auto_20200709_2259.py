# Generated by Django 2.2 on 2020-07-09 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_auto_20200703_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodpackage',
            old_name='price_per_meal',
            new_name='price_per_week_total',
        ),
        migrations.RenameField(
            model_name='foodpackage',
            old_name='price_per_month',
            new_name='price_per_week_type',
        ),
        migrations.RemoveField(
            model_name='fooddishes',
            name='package',
        ),
        migrations.RemoveField(
            model_name='foodpackage',
            name='food_type',
        ),
        migrations.CreateModel(
            name='FoodMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type', models.TextField(blank=True, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('day', models.TextField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_food_meal_package', to='Shop.FoodPackage')),
            ],
            options={
                'verbose_name': 'Food Meal',
                'verbose_name_plural': 'Food Meals',
            },
        ),
        migrations.AddField(
            model_name='fooddishes',
            name='meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_food_dishes_meal', to='Shop.FoodMeal'),
        ),
    ]
