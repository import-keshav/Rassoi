from django import forms
from rest_framework import serializers

from . import models as order_models
from Client import models as cliet_models
from Fruit import models as fruit_models
from Food import models as food_models
from Grocery import models as grocery_models
from Vegetable import models as vegetable_models
from Shop import models as shop_models


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.Order
        fields = '__all__'

    def validate(self, data):
        must_keys = [
        	'shop', 'client', 'payment_method', 'total_amount',
        	'order_type', 'slot', 'client_address_details']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class CreateOrderGrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderGrocery
        fields = '__all__'

    def validate(self, data):
        must_keys = ['order', 'grocery', 'grocery_price', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        if data['order'].shop != data['grocery'].shop:
            raise forms.ValidationError('This Grocery not belongs to the given order shop')
        if data['grocery_price'].grocery != data['grocery']:
            raise forms.ValidationError('This Grocery Price not belongs to the given Grocery')
        return data


class CreateOrderFruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderFruit
        fields = '__all__'

    def validate(self, data):
        must_keys = ['order', 'fruit', 'fruit_price', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        if data['order'].shop != data['fruit'].shop:
            raise forms.ValidationError('This Fruit not belongs to the given order shop')
        if data['fruit_price'].fruit != data['fruit']:
            raise forms.ValidationError('This Fruit Price not belongs to the given Fruit')
        return data


class CreateOrderVegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderVegetable
        fields = '__all__'

    def validate(self, data):
        must_keys = ['order', 'vegetable', 'vegetable_price', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        if data['order'].shop != data['vegetable'].shop:
            raise forms.ValidationError('This Vegetable not belongs to the given order shop')
        if data['vegetable_price'].vegetable != data['vegetable']:
            raise forms.ValidationError('This Vegetable Price not belongs to the given Vegetable')
        return data


class CreateOrderFoodMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderFoodMeal
        fields = '__all__'

    def validate(self, data):
        must_keys = ['order', 'food_meal', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        if data['order'].shop != data['food_meal'].shop:
            raise forms.ValidationError('This Food Meal not belongs to the given order shop')
        return data
