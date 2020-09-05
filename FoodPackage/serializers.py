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


class CreateFoodPackageMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_package_models.FoodPackageMeal
        fields = '__all__'


class CreateFoodPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_package_models.FoodPackage
        fields = '__all__'


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
