from django.db import models
from django.core.validators import MinValueValidator


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


class ShopPromocode(models.Model):
    promocode = models.CharField(max_length=10, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_shop_promocode_shop", null=True, blank=True)
    discount_percentage = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    valid_date = models.DateField(null=True, blank=True)
    # category = models.ManyToManyField(RestraurantDishesCategory)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Shop Promocode'
        verbose_name_plural = 'Shop Promocodes'
    def __str__(self):
        return self.promocode
