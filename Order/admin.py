from django.contrib import admin

from .models import *


class OrderGroceryTabularInline(admin.TabularInline):
	model = OrderGrocery
	extra = 1


class OrderFruitTabularInline(admin.TabularInline):
	model = OrderFruit
	extra = 1


class OrderVegetableTabularInline(admin.TabularInline):
	model = OrderVegetable
	extra = 1


class OrderFoodMealTabularInline(admin.TabularInline):
	model = OrderFoodMeal
	extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Order._meta.fields]
	search_fields = ('shop__latitude', 'shop__longitude', 'shop__id',
		'client__user__name', 'client__user__email', 'client__user__mobile',
		'client__id', 'delivered_time', 'id', 'created')
	list_filter = ('shop', 'order_type')
	inlines = (
		OrderGroceryTabularInline,
		OrderFruitTabularInline,
		OrderVegetableTabularInline,
		OrderFoodMealTabularInline
	)


@admin.register(OnGoingOrders)
class OnGoingOrdersAdmin(admin.ModelAdmin):
	list_display = [field.name for field in OnGoingOrders._meta.fields]


@admin.register(FoodPackageEachMealOrder)
class FoodPackageEachMealOrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in FoodPackageEachMealOrder._meta.fields]
