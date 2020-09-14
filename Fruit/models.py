from django.db import models
from django.core.validators import MinValueValidator

from Shop import models as shop_models

PRICES_TYPE = (
    ('Dozen', 'Dozen'),
    ('Kg', 'Kg'),
)


class Fruit(models.Model):
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="fruit_fruit_shop", null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    is_available = models.BooleanField(default=False, null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Fruit'
        verbose_name_plural = 'Fruites'
    def __str__(self):
        return self.name


class FruitPrice(models.Model):
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE, related_name="fruit_fruit_price_fruit", null=True, blank=True)
    price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    amount = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    price_type = models.TextField(choices=PRICES_TYPE, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Fruit Price'
        verbose_name_plural = 'Fruit Price'
