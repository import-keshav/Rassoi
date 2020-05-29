from django.contrib import admin

from .models import (
	Driver, DriverNotification
)

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
	list_display = ('user', 'shop_assigned', 'is_free', 'id')
	search_fields = ('user__name', 'user__email', 'user__mobile', 'user__id',
		'shop_assigned', 'is_free', 'id')
	list_filter = ('shop_assigned', 'is_free')


@admin.register(DriverNotification)
class DriverNotificationAdmin(admin.ModelAdmin):
	list_display = ('driver', 'date', 'time', 'notification_text', 'id')
	search_fields = (
		'driver__user__name', 'driver__user__email', 'driver__user__mobile', 'driver__id',
		'time', 'notification_text', 'id')