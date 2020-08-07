from django.contrib import admin

from .models import *


# @admin.register(ShopPromocode)
# class ShopPromocodeAdmin(admin.ModelAdmin):
# 	list_display = ('promocode', 'shop', 'discount_percentage', 'valid_date',
# 		'maximum_discount_price', 'maximum_number_of_usage', 'category', 'id')
# 	search_fields = ('id', 'shop__id', 'shop__name', 'promocode', 'valid_date')
# 	list_filter = ('shop', 'valid_date',)
