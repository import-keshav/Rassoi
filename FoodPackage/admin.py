from django.contrib import admin

from .models import *


class FoodPackageMealTabularInline(admin.TabularInline):
	model = FoodPackageMeal
	extra = 1


@admin.register(FoodPackage)
class FoodPackageAdmin(admin.ModelAdmin):
	list_display = ('client', 'shop', 'start_date', 'end_date', 'id')
	search_fields = ('client', 'shop', 'id',)
	list_filter = ('shop',)
	inlines = (FoodPackageMealTabularInline,)
