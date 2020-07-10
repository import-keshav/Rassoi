from django.contrib import admin

from .models import (
	GroceryApproval,
	FruitApproval,
	VegetableApproval,
	FoodPackageApproval
)


@admin.register(GroceryApproval)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('grocery', 'get_shop_name', 'is_approved', 'action', 'id')
	search_fields = ('id',)
	def get_shop_name(self, obj):
		return obj.grocery.shop
	get_shop_name.short_description = 'Shop Name'


@admin.register(FruitApproval)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('fruit', 'get_shop_name', 'is_approved', 'action', 'id')
	search_fields = ('id',)
	def get_shop_name(self, obj):
		return obj.fruit.shop
	get_shop_name.short_description = 'Shop Name'


@admin.register(VegetableApproval)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('vegetable', 'get_shop_name', 'is_approved', 'action', 'id')
	search_fields = ('id',)
	def get_shop_name(self, obj):
		return obj.vegetable.shop
	get_shop_name.short_description = 'Shop Name'


@admin.register(FoodPackageApproval)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('food_package', 'get_shop_name', 'is_approved', 'action', 'id')
	search_fields = ('id',)
	def get_shop_name(self, obj):
		return obj.food_package.shop
	get_shop_name.short_description = 'Shop Name'