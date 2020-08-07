from django import forms
from rest_framework import serializers

from . import models as grocery_models


class GetGroceryPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = grocery_models.GroceryPrice
        fields = '__all__'


class ListGroceriesSerializer(serializers.ModelSerializer):
    prices = serializers.SerializerMethodField()

    def get_prices(self, obj):
        items = grocery_models.GroceryPrice.objects.filter(grocery=obj)
        return [GetGroceryPriceSerializer(item).data for item in items]

    class Meta:
        model = grocery_models.Grocery
        fields = '__all__'


class CreateGrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = grocery_models.Grocery
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'name']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data