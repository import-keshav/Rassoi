from django.db import models
from django.core.validators import MinValueValidator

from Client import models as cliet_models
from Food import models as food_models
from Shop import models as shop_models

FOOD_TYPE = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
)


class FoodPackage(models.Model):
    client = models.ForeignKey(cliet_models.Client, on_delete=models.CASCADE, related_name="food_package_food_package_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="food_package_food_package_shop", null=True, blank=True)
    food_type = models.TextField(choices=FOOD_TYPE, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Food Package'
        verbose_name_plural = 'Food Packages'


class FoodPackageMeal(models.Model):
    food_package = models.ForeignKey(FoodPackage, on_delete=models.CASCADE, related_name="food_package_food_package_meals_food_package", null=True, blank=True)
    meal = models.ForeignKey(food_models.FoodMeal, on_delete=models.CASCADE, related_name="food_package_food_package_meals_meal", null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Food Package Meal'
        verbose_name_plural = 'Food Package Meal'
