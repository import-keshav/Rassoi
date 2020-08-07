from django import forms
from rest_framework import serializers

from . import models as client_models

class CreateShopFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ShopFeedBack
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'client', 'comment', 'number_of_stars']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListShopFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ShopFeedBack
        fields = '__all__'
