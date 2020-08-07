from django.contrib import admin

from .models import *


class FruitPriceTabularInline(admin.TabularInline):
	model = FruitPrice
	extra = 1

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
	list_display = ('name', 'shop', 'is_available', 'is_approved', 'id')
	search_fields = ('name', 'shop', 'id',)
	list_filter = ('name', 'shop', 'is_available',)
	inlines = (FruitPriceTabularInline,)