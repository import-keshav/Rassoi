from django.contrib import admin

from .models import *


class FoodDishesTabularInline(admin.TabularInline):
	model = FoodDishes
	extra = 1


@admin.register(FoodMeal)
class FoodMealAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'food_type', 'day', 'image', 
		'is_available', 'is_approved', 'id')
	search_fields = ('name', 'food_type', 'day', 'id')
	list_filter = ('food_type', 'day', 'shop')
	inlines = (FoodDishesTabularInline,)
