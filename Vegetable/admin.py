from django.contrib import admin

from .models import *


@admin.register(Vegetable)
class VegetableAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'price_per_kg', 'is_available', 'is_approved', 'id')
	search_fields = ('name', 'shop', 'id',)
	list_filter = ('name', 'shop', 'is_available',)