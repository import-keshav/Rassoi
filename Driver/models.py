from django.db import models

from User import models as user_models
from Shop import models as shop_models

class Driver(models.Model):
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE, related_name="driver_driver_user", null=True, blank=True)
    shop_assigned = models.ForeignKey(shop_models.Shop, on_delete=models.CASCADE, related_name="driver_driver_shop", null=True, blank=True)
    is_free = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
    def __str__(self):
        return self.user.name


class DriverNotification(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="driver_driver_notification_client", null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    notification_text = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Driver Notification'
        verbose_name_plural = 'Driver Notifications'
