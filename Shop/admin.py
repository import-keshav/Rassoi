from django.contrib import admin

from .models import (
	Shop, ShopPromocode, Grocery, Fruit, Vegetable, FoodPackage,
	FoodDishes, Slots, GroceryPrice, FoodMeal
)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('address', 'location_coordinates', 'is_open', 'image', 'unique_id', 'id')
	search_fields = ('location_coordinates', 'address', 'id',)


@admin.register(ShopPromocode)
class ShopPromocodeAdmin(admin.ModelAdmin):
	list_display = ('promocode', 'shop', 'discount_percentage', 'valid_date',
		'maximum_discount_price', 'maximum_number_of_usage', 'category', 'id')
	search_fields = ('id', 'shop__id', 'shop__name', 'promocode', 'valid_date')
	list_filter = ('shop', 'valid_date',)


class GroceryPriceTabularInline(admin.TabularInline):
	model = GroceryPrice
	extra = 1


@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'is_available', 'is_approved','id')
	search_fields = ('name', 'shop', 'id',)
	list_filter = ('name', 'shop', 'is_available',)
	inlines = (GroceryPriceTabularInline,)


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_dozen', 'price_per_kg',
		'is_available', 'is_approved', 'id')
	search_fields = ('name', 'shop', 'id',)
	list_filter = ('name', 'shop', 'is_available',)


@admin.register(Vegetable)
class FruitAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_kg', 'is_available', 'is_approved', 'id')
	search_fields = ('name', 'shop', 'id',)
	list_filter = ('name', 'shop', 'is_available',)


class FoodMealTabularInline(admin.TabularInline):
	model = FoodMeal
	extra = 1
	show_change_link = True

class FoodDishesTabularInline(admin.TabularInline):
	model = FoodDishes
	extra = 1

@admin.register(FoodPackage)
class FoodPackageAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_week_total', 'price_per_week_type',
		'is_available', 'is_approved', 'id')
	search_fields = ('name', 'shop', 'id',)
	# inlines = (FoodMealTabularInline,)
	list_filter = ('name', 'shop', 'is_available',)


@admin.register(FoodMeal)
class FoodMealAdmin(admin.ModelAdmin):
	list_display = ('name', 'food_type', 'day', 'image', 'id')
	search_fields = ('name', 'food_type', 'day', 'id')
	list_filter = ('food_type', 'day')
	inlines = (FoodDishesTabularInline,)


@admin.register(Slots)
class SlotsAdmin(admin.ModelAdmin):
	list_display = ('shop', 'category', 'start_time', 'end_time',
		'date', 'id')
	search_fields = ('shop', 'category', 'start_time', 'end_time',
		'date', 'id')
	list_filter = ('shop', 'category')


# @admin.register(FoodPackageClientSubscription)
# class SlotsAdmin(admin.ModelAdmin):
# 	list_display = ('client', 'food_package', 'food_types', 'start_date',
# 		'end_date', 'id',)
# 	search_fields = ('client__user__name', 'client__user__email',
# 		'food_package__name', 'id')
# 	list_filter = ('food_types',)
