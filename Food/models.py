from django.db import models
from django.core.validators import MinValueValidator

from Shop import models as shop_models

FOOD_TYPE = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
)


class FoodMeal(models.Model):
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="food_food_meal_shop", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    food_type = models.TextField(choices=FOOD_TYPE, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    is_approved = models.BooleanField(default=False, null=True, blank=True)
    is_available = models.BooleanField(default=False, null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])


    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Food Meal'
        verbose_name_plural = 'Food Meals'
    def __str__(self):
        return self.name


class FoodDishes(models.Model):
    meal = models.ForeignKey(FoodMeal, on_delete=models.CASCADE, related_name="food_food_dishes_meal", null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    number_of_items = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Food Dish'
        verbose_name_plural = 'Food Dishes'
