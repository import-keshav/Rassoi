from django import forms
from rest_framework import serializers

from . import models as food_package_models
from Client import serializers as client_serializer
from Food import serializers as food_serializer
from Shop import serializers as shop_serializer


class ListFoodPackageMealSerializer(serializers.ModelSerializer):
    meal = food_serializer.ListFoodMealSerializer()

    class Meta:
        model = food_package_models.FoodPackageMeal
        fields = '__all__'


class UpdateDeleteFoodPackageMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_package_models.FoodPackageMeal
        fields = '__all__'


class CreateFoodPackageMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_package_models.FoodPackageMeal
        fields = '__all__'
    def validate(self, data):
        must_keys = ['food_package', 'meal']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        if data['food_package'].shop != data['meal'].shop:
            raise forms.ValidationError("This Meal doesn't belong to this Shop")
        self.remove_food_meals_of_same_day(data)
        return data

    def remove_food_meals_of_same_day(self, data):
        existing_meals = food_package_models.FoodPackageMeal.objects.filter(food_package=data['food_package'])
        to_be_removed_existing_meals = []
        for existing_meal in existing_meals:
            if existing_meal.meal.day == data['meal'].day:
                existing_meal.delete()


class ListFoodPackageSerializer(serializers.ModelSerializer):
    client = client_serializer.GetClientInfoSerializer()
    shop = shop_serializer.ListShop()
    meals = serializers.SerializerMethodField()
    def get_meals(self, obj):
        data = {}
        package_meals = food_package_models.FoodPackageMeal.objects.filter(food_package=obj)
        for package_meal in package_meals:
            data[package_meal.meal.day] = ListFoodPackageMealSerializer(package_meal).data
        return data

    class Meta:
        model = food_package_models.FoodPackage
        fields = '__all__'


class UpdateDeleteFoodPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_package_models.FoodPackage
        fields = '__all__'


class CreateFoodPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_package_models.FoodPackage
        fields = '__all__'
    def validate(self, data):
        must_keys = ['client', 'shop', 'start_date', 'end_date']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data
