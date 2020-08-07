from django.contrib import admin

from .models import *


class GroceryPriceTabularInline(admin.TabularInline):
	model = GroceryPrice
	extra = 1


@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'is_available', 'is_approved','id')
	search_fields = ('name', 'shop', 'id',)
	list_filter = ('name', 'shop', 'is_available',)
	inlines = (GroceryPriceTabularInline,)