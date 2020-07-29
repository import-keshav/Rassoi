from django.contrib import admin

from .models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('user', 'location_coordinates', 'address', 'id')
	search_fields = ('user__name', 'user__email', 'user__mobile', 'location_coordinates',
		'address', 'id', 'user__id')


@admin.register(ClientNotification)
class ClientNotificationAdmin(admin.ModelAdmin):
	list_display = ('client', 'date', 'time', 'notification_text', 'id')
	search_fields = (
		'client__user__name', 'client__user__email', 'client__user__mobile', 'client__id',
		'time', 'notification_text', 'id')


@admin.register(ShopFeedBack)
class ShopFeedBackAdmin(admin.ModelAdmin):
	list_display = ('client', 'comment', 'number_of_stars', 'shop', 'id',)
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('number_of_stars',)


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