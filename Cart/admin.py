from django.contrib import admin

from .models import *


@admin.register(ClientFruitCart)
class ClientFruitCartAdmin(admin.ModelAdmin):
	list_display = ('client', 'client_id', 'shop_id', 'fruit_id', 'num_of_items', 'id',)
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('shop',)
	def get_fruit_id(self):
		return self.fruit.id
	def get_shop_id(self):
		return self.shop.id
	def get_client_id(self):
		return self.client.id


@admin.register(ClientVegetableCart)
class ClientVegetableCartAdmin(admin.ModelAdmin):
	list_display = ('client', 'client_id', 'shop_id', 'vegetable_id', 'num_of_items', 'id',)
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('shop',)
	def get_vegetable_id(self):
		return self.vegetable.id
	def get_shop_id(self):
		return self.shop.id
	def get_client_id(self):
		return self.client.id


@admin.register(ClientGroceryCart)
class ClientGroceryCartAdmin(admin.ModelAdmin):
	list_display = ('client', 'client_id', 'shop_id', 'grocery_id', 'grocery_price', 'num_of_items', 'id',)
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('shop',)
	def get_grocery_id(self):
		return self.grocery.id
	def get_shop_id(self):
		return self.shop.id
	def get_client_id(self):
		return self.client.id


@admin.register(ClientFoodMealCart)
class ClientFoodMealCartAdmin(admin.ModelAdmin):
	list_display = ('client', 'client_id','shop_id', 'food_meal_id', 'num_of_items', 'id',)
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('shop',)
	def get_food_meal_id(self):
		return self.food_meal.id
	def get_shop_id(self):
		return self.shop.id
	def get_client_id(self):
		return self.client.id


@admin.register(ClientFoodPackageCart)
class ClientFoodPackageCartAdmin(admin.ModelAdmin):
	list_display = ('client', 'client_id', 'shop_id','food_package_id', 'price', 'id')
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('shop',)
	def get_food_package_id(self):
		return self.food_package.id
	def get_shop_id(self):
		return self.shop.id
	def get_client_id(self):
		return self.client.id
