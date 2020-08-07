from django import forms
from rest_framework import serializers

from . import models as client_models

from Fruit import serializers as fruit_serializer
from Food import serializers as food_serializer
from Grocery import serializers as grocery_serializer
from Shop import serializers as shop_serializer
from User import serializers as user_serializer
from Vegetable import serializers as vegetable_serializer


class GetClientInfoSerializer(serializers.ModelSerializer):
    user = user_serializer.GetUserInfoSerializer()
    class Meta:
        model = client_models.Client
        fields = '__all__'


class GetClientNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientNotification
        fields = '__all__'
