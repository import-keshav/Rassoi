from django.db import models
from django.core.validators import MinValueValidator


ITEMS = (
    ('Grocery', 'Grocery'),
    ('Fruit', 'Fruit'),
    ('Vegetable', 'Vegetable'),
    ('Food', 'Food')
)

FOOD_TYPE = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),

)
class Shop(models.Model):
    location_coordinates = models.CharField(max_length=30, null=True, blank=True)
    is_open = models.BooleanField(default=False, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
    def __str__(self):
        return self.address


class Grocery(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_grocery_shop", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    is_available = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Grocery'
        verbose_name_plural = 'Groceries'
    def __str__(self):
        return self.name


class GroceryInKgQuantityPrice(models.Model):
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE, related_name="shop_grocery_quantity_grocery", null=True, blank=True)
    amount = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Grocery Item Quantity Price'
        verbose_name_plural = 'Grocery Item Quantity Price'
    def __str__(self):
        return self.grocery.name


class GroceryInNumOfItemsPrice(models.Model):
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE, related_name="shop_grocery_items_grocery", null=True, blank=True)
    num_of_items = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Grocery In Num Of ItemsPrice'
        verbose_name_plural = 'Grocery In Num Of ItemsPrice'
    def __str__(self):
        return self.grocery.name


class Fruit(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_fruit_shop", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    price_per_dozen = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    price_per_kg = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Fruit'
        verbose_name_plural = 'Fruites'
    def __str__(self):
        return self.name


class Vegetable(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_vegetable_shop", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    price_per_kg = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Vegetable'
        verbose_name_plural = 'Vegetables'
    def __str__(self):
        return self.name


class FoodPackage(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_food_shop", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    food_type = models.TextField(choices=FOOD_TYPE, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    price_per_meal = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    price_per_month = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Food Package'
        verbose_name_plural = 'Food Packages'
    def __str__(self):
        return self.name


class FoodDishes(models.Model):
    package = models.ForeignKey(FoodPackage, on_delete=models.CASCADE, related_name="shop_food_dishes_package", null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    number_of_items = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Food Dishe'
        verbose_name_plural = 'Food Dishes'
    def __str__(self):
        return self.name


class ShopPromocode(models.Model):
    promocode = models.CharField(max_length=10, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_shop_promocode_shop", null=True, blank=True)
    discount_percentage = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    valid_date = models.DateField(null=True, blank=True)
    maximum_discount_price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    maximum_number_of_usage = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    # category = models.ManyToManyField(RestraurantDishesCategory)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Shop Promocode'
        verbose_name_plural = 'Shop Promocodes'
    def __str__(self):
        return self.promocode


class Slots(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_slots_shop", null=True, blank=True)
    category = models.TextField(choices=ITEMS, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Slot'
        verbose_name_plural = 'Slots'
    def __str__(self):
        return self.start_time
