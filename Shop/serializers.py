from django import forms
from rest_framework import serializers

from . import models as shop_models


class GetGroceryInNumOfItemsPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.GroceryInNumOfItemsPrice
        fields = '__all__'

class GetGroceryInKgQuantityPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.GroceryInKgQuantityPrice
        fields = '__all__'

class GetGroceryInLitresPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.GroceryInLitresPrice
        fields = '__all__'


class ListGroceriesSerializer(serializers.ModelSerializer):
    kg_price = serializers.SerializerMethodField()
    num_of_items_price = serializers.SerializerMethodField()
    litre_price = serializers.SerializerMethodField()

    def get_kg_price(self, obj):
        items = shop_models.GroceryInKgQuantityPrice.objects.filter(grocery=obj)
        return [GetGroceryInKgQuantityPriceSerializer(item).data for item in items]

    def get_num_of_items_price(self, obj):
        items = shop_models.GroceryInNumOfItemsPrice.objects.filter(grocery=obj)
        return [GetGroceryInNumOfItemsPriceSerializer(item).data for item in items]

    def get_litre_price(self, obj):
        items = shop_models.GroceryInLitresPrice.objects.filter(grocery=obj)
        return [GetGroceryInLitresPriceSerializer(item).data for item in items]

    class Meta:
        model = shop_models.Grocery
        fields = '__all__'


class CreateGrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Grocery
        fields = '__all__'


class ListFruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Fruit
        fields = '__all__'


class CreateFruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Fruit
        fields = '__all__'


class ListVegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Vegetable
        fields = '__all__'


class CreateVegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Vegetable
        fields = '__all__'

class ListSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Slots
        fields = '__all__'