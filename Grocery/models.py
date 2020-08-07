from django.db import models
from django.core.validators import MinValueValidator

from Shop import models as shop_models

PRICES_TYPE = (
    ('KG', 'KG'),
    ('Lts', 'Lts'),
    ('No', 'No'),
)


class Grocery(models.Model):
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="grocery_grocery_shop", null=True, blank=True)
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