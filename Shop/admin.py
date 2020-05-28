from django.contrib import admin

from .models import (
	Shop, ShopPromocode, Grocery, Fruit, Vegetable, FoodPackage,
	FoodDishes, Slots
)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('address', 'location_coordinates', 'is_open', 'image', 'id')
	search_fields = ('location_coordinates', 'address', 'id',)


@admin.register(ShopPromocode)
class ShopPromocodeAdmin(admin.ModelAdmin):
	list_display = ('promocode', 'shop', 'discount_percentage', 'valid_date', 'id')
	search_fields = ('id', 'shop__id', 'shop__name', 'promocode', 'valid_date')


@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_item', 'price_per_kg',
		'is_available', 'id')
	search_fields = ('name', 'shop', 'id',)


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_dozen', 'price_per_kg',
		'is_available', 'id')
	search_fields = ('name', 'shop', 'id',)


@admin.register(Vegetable)
class FruitAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_kg', 'is_available', 'id')
	search_fields = ('name', 'shop', 'id',)


class FoodDishesTabularInline(admin.TabularInline):
	model = FoodDishes
	extra = 1


@admin.register(FoodPackage)
class FoodPackageAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_meal', 'price_per_month',
		'is_available', 'id')
	search_fields = ('name', 'shop', 'id',)
	inlines = (FoodDishesTabularInline,)
