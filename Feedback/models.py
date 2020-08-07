from django.db import models
from django.core.validators import MinValueValidator

from Client import models as client_models
from Shop import models as shop_models


class ShopFeedBack(models.Model):
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="shop_shop_feedback_shop", null=True, blank=True)
    client = models.ForeignKey(client_models.Client, on_delete=models.CASCADE, related_name="shop_shop_feedback_client", null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    number_of_stars = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Shop FeedBack'
        verbose_name_plural = 'Shop FeedBacks'