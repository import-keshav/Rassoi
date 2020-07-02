from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from Shop import models as shop_models
from Client import models as client_models


class ShopRating(models.Model):
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="shop_rating", null=True, blank=True)
    rating = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Shop Rating'
        verbose_name_plural = 'Shop Rating'


class ClientReview(models.Model):
    client = models.ForeignKey(client_models.Client, on_delete=models.CASCADE, related_name="reviews_client_review_client", null=True, blank=True)
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="reviews_client_review_shop", null=True, blank=True)
    points = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Client Review'
        verbose_name_plural = 'Client Reviews'
    def __str__(self):
        return self.client.user.name


class ShopReviewsInfo(models.Model):
    shop = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="reviews_shop_review_Shop", null=True, blank=True)
    number_of_reviews = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    points = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Shop Review Info'
        verbose_name_plural = 'Shop Reviews Info'
