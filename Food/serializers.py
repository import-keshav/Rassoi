from django import forms
from rest_framework import serializers

from . import models as food_models


class ListFoodDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.FoodDishes
        fields = '__all__'


class CreateFoodDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.FoodDishes
        fields = '__all__'
    def validate(self, data):
        must_keys = ['meal', 'name', 'number_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListFoodMealSerializer(serializers.ModelSerializer):
    dishes = serializers.SerializerMethodField()
    def get_dishes(self, obj):
        dishes = food_models.FoodDishes.objects.filter(meal=obj)
        return [ListFoodDishesSerializer(dish).data for dish in dishes]

    class Meta:
        model = food_models.FoodMeal
        fields = '__all__'


class CreateFoodMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_models.FoodMeal
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'name', 'food_type', 'day', 'price']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data