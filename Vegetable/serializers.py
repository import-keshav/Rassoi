from django import forms
from rest_framework import serializers

from . import models as vegetable_models


class GetVegetablePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = vegetable_models.VegetablePrice
        fields = '__all__'


class ListVegetableSerializer(serializers.ModelSerializer):
    prices = serializers.SerializerMethodField()

    def get_prices(self, obj):
        items = vegetable_models.VegetablePrice.objects.filter(vegetable=obj)
        return [GetVegetablePriceSerializer(item).data for item in items]

    class Meta:
        model = vegetable_models.Vegetable
        fields = '__all__'


class CreateVegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = vegetable_models.Vegetable
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'name']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data
