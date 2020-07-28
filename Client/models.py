from django.db import models
from django.core.validators import MinValueValidator

from User import models as user_models
from Shop import models as shop_models

class Client(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name="client_client_user", null=True, blank=True)
    location_coordinates = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    # category = models.CharField(max_length=50, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    def __str__(self):
        return self.user.name


class ClientNotification(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_client_notification_client", null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    notification_text = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Notification'
        verbose_name_plural = 'Client Notifications'


class ClientFruitCart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_client_fruit_cart_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="client_client_fruit_cart_shop", null=True, blank=True)
    fruit = models.ForeignKey(shop_models.Fruit, on_delete=models.CASCADE, related_name="client_client_fruit_cart_fruit", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Fruit Cart'
        verbose_name_plural = 'Client Fruit Carts'


class ClientVegetableCart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_client_vegetable_cart_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="client_client_vegetable_cart_shop", null=True, blank=True)
    vegetable = models.ForeignKey(shop_models.Vegetable, on_delete=models.CASCADE, related_name="client_client_vegetable_cart_vegetable", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Vegetable Cart'
        verbose_name_plural = 'Client Vegetable Carts'


class ClientGroceryCart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_client_grocery_cart_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="client_client_grocery_cart_shop", null=True, blank=True)
    grocery = models.ForeignKey(shop_models.Grocery, on_delete=models.CASCADE, related_name="client_client_grocery_cart_grocery", null=True, blank=True)
    grocery_price = models.ForeignKey(shop_models.GroceryPrice, on_delete=models.CASCADE, related_name="client_client_grocery_cart_grocery_price", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Grocery Cart'
        verbose_name_plural = 'Client Grocery Carts'


class ClientFoodMealCart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_client_food_meal_cart_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="client_client_food_meal_cart_shop", null=True, blank=True)
    food_meal = models.ForeignKey(shop_models.FoodMeal, on_delete=models.CASCADE, related_name="client_client_food_meal_cart_grocery", null=True, blank=True)
    num_of_items = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Food Meal Cart'
        verbose_name_plural = 'Client Food Meal Carts'

# class FoodPackageClientSubscription(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="shop_food_package_client_subscription_client", null=True, blank=True)
#     food_package = models.ForeignKey(FoodPackage, on_delete=models.CASCADE, related_name="shop_food_package_client_subscription_food_subscription", null=True, blank=True)
#     food_types = models.CharField(max_length=100, null=True, blank=True)
#     start_date = models.DateField(null=True, blank=True)
#     end_date = models.DateField(null=True, blank=True)


#     created = models.DateTimeField(auto_now_add=True, editable=False)
#     last_updated = models.DateTimeField(auto_now=True, editable=False)
#     class Meta:
#         verbose_name = 'Food Package Client Subscription'
#         verbose_name_plural = 'Food Package Client Subscriptions'

#     def set_food_types(self, x):
#         self.food_types = json.dumps(x)

#     def get_food_types(self):
#         return json.loads(self.food_types)


class ShopFeedBack(models.Model):
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="shop_shop_feedback_shop", null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="shop_shop_feedback_client", null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    number_of_stars = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Shop FeedBack'
        verbose_name_plural = 'Shop FeedBacks'