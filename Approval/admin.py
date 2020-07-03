from django.contrib import admin

from .models import (
	GroceryApproval,
)


@admin.register(GroceryApproval)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('grocery', 'get_shop_name', 'is_approved', 'action', 'id')
	search_fields = ('id',)
	def get_shop_name(self, obj):
		return obj.grocery.shop
	get_shop_name.short_description = 'Shop Name'