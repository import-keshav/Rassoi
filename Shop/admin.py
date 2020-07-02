from django.contrib import admin

from .models import (
	Shop, ShopPromocode, Grocery, Fruit, Vegetable, FoodPackage,
	FoodDishes, Slots, GroceryInKgQuantityPrice, GroceryInNumOfItemsPrice,
	GroceryInLitresPrice
)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('address', 'location_coordinates', 'is_open', 'image', 'id')
	search_fields = ('location_coordinates', 'address', 'id',)


@admin.register(ShopPromocode)
class ShopPromocodeAdmin(admin.ModelAdmin):
	list_display = ('promocode', 'shop', 'discount_percentage', 'valid_date', 'id')
	search_fields = ('id', 'shop__id', 'shop__name', 'promocode', 'valid_date')
	list_filter = ('shop', 'valid_date',)


class GroceryInKgQuantityPriceTabularInline(admin.TabularInline):
	model = GroceryInKgQuantityPrice
	extra = 1

class GroceryInNumOfItemsPriceTabularInline(admin.TabularInline):
	model = GroceryInNumOfItemsPrice
	extra = 1

class GroceryInLitresPriceTabularInline(admin.TabularInline):
	model = GroceryInLitresPrice
	extra = 1


@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'is_available', 'id')
	search_fields = ('name', 'shop', 'id',)
	list_filter = ('name', 'shop', 'is_available',)
	inlines = (
		GroceryInKgQuantityPriceTabularInline,
		GroceryInNumOfItemsPriceTabularInline,
		GroceryInLitresPriceTabularInline)


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_dozen', 'price_per_kg',
		'is_available', 'id')
	search_fields = ('name', 'shop', 'id',)
	list_filter = ('name', 'shop', 'is_available',)


@admin.register(Vegetable)
class FruitAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_kg', 'is_available', 'id')
	search_fields = ('name', 'shop', 'id',)
	list_filter = ('name', 'shop', 'is_available',)


class FoodDishesTabularInline(admin.TabularInline):
	model = FoodDishes
	extra = 1


@admin.register(FoodPackage)
class FoodPackageAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_meal', 'price_per_month',
		'is_available', 'id')
	search_fields = ('name', 'shop', 'id',)
	inlines = (FoodDishesTabularInline,)
	list_filter = ('name', 'shop', 'is_available',)


@admin.register(Slots)
class SlotsAdmin(admin.ModelAdmin):
	list_display = ('shop', 'category', 'start_time', 'end_time',
		'date', 'id')
	search_fields = ('shop', 'category', 'start_time', 'end_time',
		'date', 'id')
	list_filter = ('shop', 'category')
