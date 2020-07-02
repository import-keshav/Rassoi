from django.contrib import admin

from .models import (
	ShopRating,
	ClientReview,
	ShopReviewsInfo
)

@admin.register(ShopRating)
class ShopRatingAdmin(admin.ModelAdmin):
	list_display = ('shop', 'rating', 'id')
	search_fields = ('rating', 'id')


@admin.register(ClientReview)
class ClientReviewAdmin(admin.ModelAdmin):
	list_display = ('client', 'shop', 'points', 'comment', 'id')
	search_fields = ( 'client__user__name', 'client__user__email', 'client__user__mobile', 
		'client__id', 'comment', 'id')


@admin.register(ShopReviewsInfo)
class ShopReviewsInfoAdmin(admin.ModelAdmin):
	list_display = ('shop', 'number_of_reviews', 'points', 'id')
	search_fields = ('shop__id', 'id')
