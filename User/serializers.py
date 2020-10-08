from django import forms
from rest_framework import serializers

from . import models as user_models

class GetUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = ['name', 'email', 'mobile', 'avatar']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.User
        fields = '__all__'
