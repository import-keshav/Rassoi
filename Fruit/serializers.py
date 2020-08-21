from django import forms
from rest_framework import serializers

from . import models as fruit_models
from Cart import models as cart_models


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


class ListFruitsOnClientSideSerializer(serializers.ModelSerializer):
    prices = serializers.SerializerMethodField()
    is_in_cart = serializers.SerializerMethodField()

    def get_is_in_cart(self, obj):
        fruit = cart_models.ClientFruitCart.objects.filter(fruit=obj, client__pk=int(self.context['view'].kwargs['client'])).first()
        if fruit:
            return True
        return False

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
