from django.contrib import admin

from .models import *

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
	list_display = ('address', 'latitude', 'longitude', 'is_open', 'image', 'unique_id', 'id')
	search_fields = ('location_coordinates', 'address', 'id',)


@admin.register(Slots)
class SlotsAdmin(admin.ModelAdmin):
	list_display = ('shop', 'category', 'start_time', 'end_time',
		'date', 'id')
	search_fields = ('shop', 'category', 'start_time', 'end_time',
		'date', 'id')
	list_filter = ('shop', 'category')
