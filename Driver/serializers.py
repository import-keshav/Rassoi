from django import forms
from rest_framework import serializers

from . import models as driver_models
from User import serializers as user_serializer

class ListDriverSerializer(serializers.ModelSerializer):
    user = user_serializer.GetUserInfoSerializer()
    class Meta:
        model = driver_models.Driver
        fields = '__all__'