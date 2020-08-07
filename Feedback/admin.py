from django.contrib import admin

from .models import *

@admin.register(ShopFeedBack)
class ShopFeedBackAdmin(admin.ModelAdmin):
	list_display = ('client', 'comment', 'number_of_stars', 'shop', 'id',)
	search_fields = ('client__user__name', 'client__user__email')
	list_filter = ('number_of_stars',)
