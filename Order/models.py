from django.db import models
from django.core.validators import MinValueValidator


from Client import models as cliet_models
from Fruit import models as fruit_models
from Food import models as food_models
from FoodPackage import models as food_package_models
from Grocery import models as grocery_models
from Vegetable import models as vegetable_models
from Promocode import models as promocode_models
from Shop import models as shop_models

order_status = (
    ("packaging", "packaging"),
    ("on_way", "on_way"),
    ("delivered", "delivered"),
    ("food_package", "food_package")
)

order_type = (
    ("Food", "Food"),
    ("Fruit", "Fruit"),
    ("Vegetable", "Vegetable"),
    ("Grocery", "Grocery"),
    ("FoodPackage", "FoodPackage")
)

payment_choices = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Online Payment", "Online Payment"),
)

class Order(models.Model):
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="order_order_shop", null=True, blank=True)
    client = models.ForeignKey(cliet_models.Client, on_delete=models.CASCADE, related_name="order_order_client", null=True, blank=True)
    payment_method = models.TextField(choices=payment_choices, null=True, blank=True)
    is_delivered = models.BooleanField(default=False, null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    # transaction_id
    order_type = models.TextField(choices=order_type, null=True, blank=True)
    status = models.TextField(choices=order_status, null=True, blank=True)
    promocode_used = models.ForeignKey(promocode_models.ShopPromocode, on_delete=models.CASCADE, related_name="orders_order_promocode_used", null=True, blank=True)
    client_address_details = models.TextField(null=True, blank=True)
    slot = models.ForeignKey(shop_models.Slots, on_delete=models.CASCADE, related_name="orders_order_slot", null=True, blank=True)
    delivered_time = models.DateTimeField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'


class OrderGrocery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_order_grocery_order", null=True, blank=True)
    grocery = models.ForeignKey(grocery_models.Grocery, on_delete=models.CASCADE, related_name="order_order_grocery_grocery", null=True, blank=True)
    grocery_price = models.ForeignKey(grocery_models.GroceryPrice, on_delete=models.CASCADE, related_name="order_order_grocery_grocery_price", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Order Grocery'
        verbose_name_plural = 'Order Groceries'


class OrderFruit(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_order_fruit_order", null=True, blank=True)
    fruit = models.ForeignKey(fruit_models.Fruit, on_delete=models.CASCADE, related_name="order_order_fruit_fruit", null=True, blank=True)
    fruit_price = models.ForeignKey(fruit_models.FruitPrice, on_delete=models.CASCADE, related_name="order_order_fruit_fruit_price", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Order Fruit'
        verbose_name_plural = 'Order Fruites'


class OrderVegetable(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_order_vegetable_order", null=True, blank=True)
    vegetable = models.ForeignKey(vegetable_models.Vegetable, on_delete=models.CASCADE, related_name="order_order_vegetable_vegetable", null=True, blank=True)
    vegetable_price = models.ForeignKey(vegetable_models.VegetablePrice, on_delete=models.CASCADE, related_name="order_order_vegetable_vegetable_price", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Order Vegetable'
        verbose_name_plural = 'Order Vegetables'


class OrderFoodMeal(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_order_food_meal_order", null=True, blank=True)
    food_meal = models.ForeignKey(food_models.FoodMeal, on_delete=models.CASCADE, related_name="order_order_food_meal_food_meal", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Order FoodMeal'
        verbose_name_plural = 'Order FoodMeals'


class OnGoingOrders(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders_ongoing_order_order", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="orders_ongoing_order_shop", null=True, blank=True)

    class Meta:
        verbose_name = 'Ongoing Order'
        verbose_name_plural = 'Ongoing Orders'


class FoodPackageEachMealOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_food_package_meal_order_order", null=True, blank=True)
    food_package = models.ForeignKey(food_package_models.FoodPackage, on_delete=models.CASCADE, related_name="order_food_package_meal_order_food_package", null=True, blank=True)
    food_meal = models.ForeignKey(food_models.FoodMeal, on_delete=models.CASCADE, related_name="order_food_package_meal_order_food_meal", null=True, blank=True)
    status = models.TextField(choices=order_status, null=True, blank=True)
    delivered_time = models.DateTimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Food Package Each Meal Order'
        verbose_name_plural = 'Food Package Each Meal Orders'
