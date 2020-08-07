from django.contrib import admin

from .models import *


@admin.register(ClientFruitCart)
class ClientFruitCartAdmin(admin.ModelAdmin):
	list_display = ('client', 'shop', 'fruit', 'num_of_items', 'id',)
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('shop',)


@admin.register(ClientVegetableCart)
class ClientVegetableCartAdmin(admin.ModelAdmin):
	list_display = ('client', 'shop', 'vegetable', 'num_of_items', 'id',)
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('shop',)


@admin.register(ClientGroceryCart)
class ClientGroceryCartAdmin(admin.ModelAdmin):
	list_display = ('client', 'shop', 'grocery', 'grocery_price', 'num_of_items', 'id',)
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('shop',)


@admin.register(ClientFoodMealCart)
class ClientFoodMealCartAdmin(admin.ModelAdmin):
	list_display = ('client', 'shop', 'food_meal', 'num_of_items', 'id',)
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('shop',)