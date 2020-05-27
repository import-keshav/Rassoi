from django.contrib import admin

from .models import (
	Client, ClientNotification
)

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
