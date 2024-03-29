from django import forms
from rest_framework import serializers

from . import models as promocode_models


class CreateShopPromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = promocode_models.ShopPromocode
        fields = '__all__'
    def validate(self, data):
        must_keys = ['promocode', 'shop', 'discount_percentage',
            'valid_date', 'maximum_discount_price', 'category']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListShopPromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = promocode_models.ShopPromocode
        fields = '__all__'
