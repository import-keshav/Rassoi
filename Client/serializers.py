from django import forms
from rest_framework import serializers

from . import models as client_models

from User import serializers as user_serializer

class GetClientInfoSerializer(serializers.ModelSerializer):
    user = user_serializer.GetUserInfoSerializer()
    class Meta:
        model = client_models.Client
        fields = '__all__'


class GetClientNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientNotification
        fields = '__all__'
