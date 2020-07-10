from django import forms
from rest_framework import serializers

from . import models as driver_models

class ListDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = driver_models.Driver
        fields = '__all__'