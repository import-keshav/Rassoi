from django.contrib import admin

from .models import (
	Shop,
	ShopPromocode,
)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('location_coordinates', 'is_open', 'address', 'image', 'id')
	search_fields = ('location_coordinates', 'address', 'id',)


@admin.register(ShopPromocode)
class ShopPromocodeAdmin(admin.ModelAdmin):
	list_display = ('promocode', 'shop', 'discount_percentage', 'valid_date', 'id')
	search_fields = ('id', 'shop__id', 'shop__name', 'promocode', 'valid_date')
