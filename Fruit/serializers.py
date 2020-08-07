from django import forms
from rest_framework import serializers

from . import models as fruit_models


class GetFruitPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = fruit_models.FruitPrice
        fields = '__all__'


class ListFruitsSerializer(serializers.ModelSerializer):
    prices = serializers.SerializerMethodField()

    def get_prices(self, obj):
        items = fruit_models.FruitPrice.objects.filter(fruit=obj)
        return [GetFruitPriceSerializer(item).data for item in items]

    class Meta:
        model = fruit_models.Fruit
        fields = '__all__'


class CreateFruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = fruit_models.Fruit
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'name']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data
