from django.db import models
from django.core.validators import MinValueValidator

from User import models as user_models

from Shop import models as shop_models


class Client(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name="client_client_user", null=True, blank=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    # category = models.CharField(max_length=50, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    def __str__(self):
        return self.user.name


class ClientNotification(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_client_notification_client", null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    notification_text = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Client Notification'
        verbose_name_plural = 'Client Notifications'
