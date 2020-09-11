from django.db import models

from django.core.validators import MinValueValidator

from Client import models as cliet_models
from Fruit import models as fruit_models
from Food import models as food_models
from FoodPackage import models as food_package_models
from Grocery import models as grocery_models
from Vegetable import models as vegetable_models
from Shop import models as shop_models


class ClientFruitCart(models.Model):
    client = models.ForeignKey(cliet_models.Client, on_delete=models.CASCADE, related_name="cart_client_fruit_cart_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="cart_client_fruit_cart_shop", null=True, blank=True)
    fruit = models.ForeignKey(fruit_models.Fruit, on_delete=models.CASCADE, related_name="cart_client_fruit_cart_fruit", null=True, blank=True)
    fruit_price = models.ForeignKey(fruit_models.FruitPrice, on_delete=models.CASCADE, related_name="cart_client_fruit_cart_fruit_price", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Fruit Cart'
        verbose_name_plural = 'Client Fruit Carts'


class ClientVegetableCart(models.Model):
    client = models.ForeignKey(cliet_models.Client, on_delete=models.CASCADE, related_name="cart_client_vegetable_cart_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="cart_client_vegetable_cart_shop", null=True, blank=True)
    vegetable = models.ForeignKey(vegetable_models.Vegetable, on_delete=models.CASCADE, related_name="cart_client_vegetable_cart_vegetable", null=True, blank=True)
    vegetable_price = models.ForeignKey(vegetable_models.VegetablePrice, on_delete=models.CASCADE, related_name="cart_client_vegetable_cart_vegetable_price", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Vegetable Cart'
        verbose_name_plural = 'Client Vegetable Carts'


class ClientGroceryCart(models.Model):
    client = models.ForeignKey(cliet_models.Client, on_delete=models.CASCADE, related_name="cart_client_grocery_cart_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="cart_client_grocery_cart_shop", null=True, blank=True)
    grocery = models.ForeignKey(grocery_models.Grocery, on_delete=models.CASCADE, related_name="cart_client_grocery_cart_grocery", null=True, blank=True)
    grocery_price = models.ForeignKey(grocery_models.GroceryPrice, on_delete=models.CASCADE, related_name="cart_client_grocery_cart_grocery_price", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Grocery Cart'
        verbose_name_plural = 'Client Grocery Carts'


class ClientFoodMealCart(models.Model):
    client = models.ForeignKey(cliet_models.Client, on_delete=models.CASCADE, related_name="cart_client_food_meal_cart_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="cart_client_food_meal_cart_shop", null=True, blank=True)
    food_meal = models.ForeignKey(food_models.FoodMeal, on_delete=models.CASCADE, related_name="cart_client_food_meal_cart_grocery", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Food Meal Cart'
        verbose_name_plural = 'Client Food Meal Carts'


class ClientFoodPackageCart(models.Model):
    client = models.ForeignKey(cliet_models.Client, on_delete=models.CASCADE, related_name="cart_client_food_package_cart_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="cart_client_food_package_cart_shop", null=True, blank=True)
    food_package = models.ForeignKey(food_package_models.FoodPackage, on_delete=models.CASCADE, related_name="cart_client_food_package_cart_food_package", null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Food Package Cart'
        verbose_name_plural = 'Client Food Package Carts'
