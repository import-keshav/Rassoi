from django import forms
from rest_framework import serializers

from . import models as client_models

from User import serializers as user_serializer
from Shop import serializers as shop_serializer

class GetClientInfoSerializer(serializers.ModelSerializer):
    user = user_serializer.GetUserInfoSerializer()
    class Meta:
        model = client_models.Client
        fields = '__all__'


class GetClientNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientNotification
        fields = '__all__'


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


class CreateClientFruitCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientFruitCart
        fields = '__all__'
    def validate(self, data):
        must_keys = ['client', 'shop', 'fruit', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListClientFruitCartSerializer(serializers.ModelSerializer):
    fruit = shop_serializer.ListFruitsSerializer()
    client = GetClientInfoSerializer()
    class Meta:
        model = client_models.ClientFruitCart
        fields = '__all__'


class UpdateDeleteClientFruitCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientFruitCart
        fields = '__all__'


class CreateClientVegetableCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientVegetableCart
        fields = '__all__'
    def validate(self, data):
        must_keys = ['client', 'shop', 'vegetable', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListClientVegetableCartSerializer(serializers.ModelSerializer):
    vegetable = shop_serializer.ListVegetableSerializer()
    client = GetClientInfoSerializer()
    class Meta:
        model = client_models.ClientVegetableCart
        fields = '__all__'


class UpdateDeleteClientVegetableCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientVegetableCart
        fields = '__all__'


class CreateClientGroceryCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientGroceryCart
        fields = '__all__'
    def validate(self, data):
        must_keys = ['client', 'shop', 'grocery', 'grocery_price', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListClientGroceryCartSerializer(serializers.ModelSerializer):
    grocery = shop_serializer.ListGroceriesSerializer()
    grocery_price = shop_serializer.GetGroceryPriceSerializer()
    class Meta:
        model = client_models.ClientGroceryCart
        fields = '__all__'


class UpdateDeleteClientGroceryCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientGroceryCart
        fields = '__all__'


class CreateClientFoodMealCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientFoodMealCart
        fields = '__all__'
    def validate(self, data):
        must_keys = ['client', 'shop', 'food_meal', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListClientFoodMealCartSerializer(serializers.ModelSerializer):
    food_meal = shop_serializer.ListFoodMealSerializer()
    class Meta:
        model = client_models.ClientFoodMealCart
        fields = '__all__'


class UpdateDeleteClientFoodMealCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = client_models.ClientFoodMealCart
        fields = '__all__'