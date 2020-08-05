import hashlib, binascii, os, random
from django.db import models
from django.core.validators import MinValueValidator


ITEMS = (
    ('Grocery', 'Grocery'),
    ('Fruit', 'Fruit'),
    ('Vegetable', 'Vegetable'),
    ('Food', 'Food')
)


PRODUCT_CATEGORY = (
    ('Grocery', 'Grocery'),
    ('Fruit', 'Fruit'),
    ('Vegetable', 'Vegetable'),
    ('Food', 'Food')
)

PRICES_TYPE = (
    ('KG', 'KG'),
    ('Lts', 'Lts'),
    ('No', 'No'),
)

FOOD_TYPE = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
)

DAYS = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


class Shop(models.Model):
    location_coordinates = models.CharField(max_length=30, null=True, blank=True)
    is_open = models.BooleanField(default=False, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    password = models.TextField(null=True, blank=True)
    unique_id = models.CharField(max_length=100, null=True, blank=True, unique=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
    def __str__(self):
        return self.address
    def save(self):
        self.password = hash_password(self.password)
        super(Shop, self).save()


class Grocery(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_grocery_shop", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    is_available = models.BooleanField(default=True, null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Grocery'
        verbose_name_plural = 'Groceries'
    def __str__(self):
        return self.name


class GroceryPrice(models.Model):
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE, related_name="shop_grocery_price_grocery", null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    amount = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    price_type = models.TextField(choices=PRICES_TYPE, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Grocery Price'
        verbose_name_plural = 'Grocery Price'
    def __str__(self):
        return self.grocery.name


class Fruit(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_fruit_shop", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    price_per_dozen = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    price_per_kg = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=False, null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)

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
    is_approved = models.BooleanField(default=False, null=True, blank=True)

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
    image = models.FileField(null=True, blank=True, upload_to="")
    is_available = models.BooleanField(default=False, null=True, blank=True)
    price_per_week_total = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    price_per_week_type = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    is_approved = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Food Package'
        verbose_name_plural = 'Food Packages'
    def __str__(self):
        return self.name


class FoodMeal(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_food_meal_shop", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    food_type = models.TextField(choices=FOOD_TYPE, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    day =  models.TextField(choices=DAYS, null=True, blank=True)
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
    meal = models.ForeignKey(FoodMeal, on_delete=models.CASCADE, related_name="shop_food_dishes_meal", null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    number_of_items = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Food Dishe'
        verbose_name_plural = 'Food Dishes'


class ShopPromocode(models.Model):
    promocode = models.CharField(max_length=10, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_shop_promocode_shop", null=True, blank=True)
    discount_percentage = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    valid_date = models.DateField(null=True, blank=True)
    maximum_discount_price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    maximum_number_of_usage = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    category = models.TextField(choices=ITEMS, null=True, blank=True)

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

