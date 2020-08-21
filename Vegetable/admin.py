from django.contrib import admin

from .models import *


class VegetablePriceTabularInline(admin.TabularInline):
	model = VegetablePrice
	extra = 1

@admin.register(Vegetable)
class VegetableAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'is_available', 'is_approved', 'id')
	search_fields = ('name', 'shop', 'id',)
	list_filter = ('name', 'shop', 'is_available',)
	inlines = (VegetablePriceTabularInline,)
