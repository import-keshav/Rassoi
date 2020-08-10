import hashlib, binascii, os, random
from django.db import models
from django.core.validators import MinValueValidator


ITEMS = (
    ('Grocery', 'Grocery'),
    ('Fruit', 'Fruit'),
    ('Vegetable', 'Vegetable'),
    ('Food', 'Food')
)


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


class Shop(models.Model):
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    is_open = models.BooleanField(default=False, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="")
    password = models.TextField(null=True, blank=True)
    unique_id = models.CharField(max_length=100, null=True, blank=True, unique=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
    def __str__(self):
        return self.address
    def save(self):
        self.password = hash_password(self.password)
        super(Shop, self).save()


class Slots(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_slots_shop", null=True, blank=True)
    category = models.TextField(choices=ITEMS, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        verbose_name = 'Slot'
        verbose_name_plural = 'Slots'

