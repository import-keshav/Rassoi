from django import forms
from rest_framework import serializers

from . import models as cart_models
from FoodPackage import models as food_package_models

from Client import serializers as client_serializer
from Fruit import serializers as fruit_serializer
from Food import serializers as food_serializer
from FoodPackage import serializers as food_package_serializer
from Grocery import serializers as grocery_serializer
from Vegetable import serializers as vegetable_serializer


class CreateClientFruitCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_models.ClientFruitCart
        fields = '__all__'
    def validate(self, data):
        must_keys = ['client', 'shop', 'fruit', 'fruit_price', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        data['price'] = data['fruit_price'].price * data['num_of_items']
        return data


class ListClientFruitCartSerializer(serializers.ModelSerializer):
    fruit = fruit_serializer.ListFruitsSerializer()
    fruit_price = fruit_serializer.GetFruitPriceSerializer()
    client = client_serializer.GetClientInfoSerializer()
    class Meta:
        model = cart_models.ClientFruitCart
        fields = '__all__'


class UpdateDeleteClientFruitCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_models.ClientFruitCart
        fields = '__all__'


class CreateClientVegetableCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_models.ClientVegetableCart
        fields = '__all__'
    def validate(self, data):
        must_keys = ['client', 'shop', 'vegetable', 'num_of_items', 'vegetable_price']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        data['price'] = data['vegetable_price'].price * data['num_of_items']
        return data


class ListClientVegetableCartSerializer(serializers.ModelSerializer):
    vegetable = vegetable_serializer.ListVegetableSerializer()
    vegetable_price = vegetable_serializer.GetVegetablePriceSerializer()
    client = client_serializer.GetClientInfoSerializer()
    class Meta:
        model = cart_models.ClientVegetableCart
        fields = '__all__'


class UpdateDeleteClientVegetableCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_models.ClientVegetableCart
        fields = '__all__'


class CreateClientGroceryCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_models.ClientGroceryCart
        fields = '__all__'
    def validate(self, data):
        must_keys = ['client', 'shop', 'grocery', 'grocery_price', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        data['price'] = data['grocery_price'].price * data['num_of_items']
        return data


class ListClientGroceryCartSerializer(serializers.ModelSerializer):
    grocery = grocery_serializer.ListGroceriesSerializer()
    grocery_price = grocery_serializer.GetGroceryPriceSerializer()
    client = client_serializer.GetClientInfoSerializer()
    class Meta:
        model = cart_models.ClientGroceryCart
        fields = '__all__'


class UpdateDeleteClientGroceryCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_models.ClientGroceryCart
        fields = '__all__'


class CreateClientFoodMealCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_models.ClientFoodMealCart
        fields = '__all__'
    def validate(self, data):
        must_keys = ['client', 'shop', 'food_meal', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        data['price'] = data['food_meal'].price * data['num_of_items']
        return data


class ListClientFoodMealCartSerializer(serializers.ModelSerializer):
    food_meal = food_serializer.ListFoodMealSerializer()
    client = client_serializer.GetClientInfoSerializer()
    class Meta:
        model = cart_models.ClientFoodMealCart
        fields = '__all__'


class UpdateDeleteClientFoodMealCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_models.ClientFoodMealCart
        fields = '__all__'


class CreateClientFoodPackageCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_models.ClientFoodPackageCart
        fields = '__all__'
    def validate(self, data):
        must_keys = ['client', 'shop', 'food_package']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        cart_models.ClientFoodPackageCart.objects.filter(client=data['client']).delete()
        food_package_meals = food_package_models.FoodPackageMeal.objects.filter(food_package=data['food_package'])
        price = 0
        for food_package_meal in food_package_meals:
            price += food_package_meal.meal.price
        data['price'] = price
        return data


class ListClientFoodPackageCartSerializer(serializers.ModelSerializer):
    food_package = food_package_serializer.ListFoodPackageSerializer()
    client = client_serializer.GetClientInfoSerializer()
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        food_package_meals = food_package_models.FoodPackageMeal.objects.filter(food_package=obj.food_package)
        price = 0
        for food_package_meal in food_package_meals:
            price += food_package_meal.meal.price
        return price
    class Meta:
        model = cart_models.ClientFoodPackageCart
        fields = '__all__'


class UpdateDeleteClientFoodPackageCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_models.ClientFoodPackageCart
        fields = '__all__'
