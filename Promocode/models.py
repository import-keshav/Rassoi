from django.db import models



# class ShopPromocode(models.Model):
#     promocode = models.CharField(max_length=10, null=True, blank=True)
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_shop_promocode_shop", null=True, blank=True)
#     discount_percentage = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
#     valid_date = models.DateField(null=True, blank=True)
#     maximum_discount_price = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
#     maximum_number_of_usage = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
#     category = models.TextField(choices=ITEMS, null=True, blank=True)

#     created = models.DateTimeField(auto_now_add=True, editable=False)
#     last_updated = models.DateTimeField(auto_now=True, editable=False)
#     class Meta:
#         verbose_name = 'Shop Promocode'
#         verbose_name_plural = 'Shop Promocodes'
#     def __str__(self):
#         return self.promocode