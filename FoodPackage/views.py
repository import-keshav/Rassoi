import datetime
from django import forms
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics, status

from . import models as food_package_models
from . import serializers as food_package_serializer
from Food import models as food_models

class ListClientFoodPackage(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.ListFoodPackageSerializer

    def get_queryset(self):
        return food_package_models.FoodPackage.objects.filter(client__pk=self.kwargs['pk'])


class CreateFoodPackage(APIView):
    def post(self, request):
        request_data_validation = self.is_request_data_valid(self.request.data)
        if not request_data_validation["is_valid"]:
            raise forms.ValidationError(request_data_validation["message"])

        package_dict = self.request.data['food_package']
        food_package_data_validation = self.is_food_package_data_valid(package_dict)
        if not request_data_validation["is_valid"]:
            raise forms.ValidationError(food_package_data_validation["message"])

        if not isinstance(self.request.data['food_meal'], list):
            raise forms.ValidationError('Food Meal key should be List')

        food_meal_validation = self.is_food_meal_valid(self.request.data['food_meal'], package_dict)
        if not food_meal_validation["is_valid"]:
            raise forms.ValidationError(food_meal_validation["message"])


        data = package_dict
        current_date = datetime.datetime.strptime(data['start_date'], "%Y-%m-%d").date()
        num_of_days = 7*int(data['num_of_weeks']) - 1
        time_delta = datetime.timedelta(days=num_of_days)
        end_date = current_date + time_delta
        data['end_date'] = end_date.strftime(format="%Y-%m-%d")
        data.pop('num_of_weeks')

        food_package_serializer_obj = food_package_serializer.CreateFoodPackageSerializer(
            data=data)
        if food_package_serializer_obj.is_valid():
            food_package_serializer_obj.save()
            food_meals = self.request.data['food_meal']
            for food_meal in food_meals:
                food_package_meal_serializer_obj = food_package_serializer.CreateFoodPackageMealSerializer(
                    data = {
                        "food_package":food_package_serializer_obj.data['id'],
                        "meal": food_meal
                })
                if food_package_meal_serializer_obj.is_valid():
                    food_package_meal_serializer_obj.save()
            return Response(food_package_serializer_obj.data)
        else:
            return Response(
                food_package_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


    def is_food_meal_valid(self, food_meals, food_package):
        map_days = {}
        if len(food_meals) < 7 or len(food_meals) >7:
            return {
                "is_valid": False,
                "message": "There should be total 7 meals, not more not less"
            }
        for food_meal in food_meals:
            food_meal_inst = food_models.FoodMeal.objects.filter(pk=food_meal).first()
            if not food_meal_inst:
                return {
                "is_valid": False,
                "message": "Food Meal Didn't Exists"
            }
            if int(food_meal_inst.shop.pk) != int(food_package["shop"]):
                return {
                "is_valid": False,
                "message": "Food Meal doesn't belong to given shop"
            }
            if food_meal_inst.day in map_days:
                return {
                "is_valid": False,
                "message": "1 day can't have 2 Food Meals"
            }
            if food_meal_inst.food_type != food_package['food_package']:
                return {
                    "is_valid": False,
                    "message": "Food Meal Type not equals Food Package Type"
                }   
            map_days[food_meal_inst.day] = 1
        return {
            "is_valid": True,
            "message": "Food Meal validated Successfully"
        }

    def is_request_data_valid(self, data):
        must_keys = ['food_package', 'food_meal']
        for key in must_keys:
            if not key in data:
                return {
                    "is_valid": False,
                    "message": 'Include ' + key + ' in data'
                }
        return {
            "is_valid": True,
            "message": "Data validated Successfully"
        }

    def is_food_package_data_valid(self, package_dict):
        must_keys = ['client', 'shop', 'start_date', 'num_of_weeks']
        for key in must_keys:
            if not key in package_dict:
                return {
                    "is_valid": False,
                    "message": 'Include ' + key + ' in Food Package data'
                }
        return {
            "is_valid": True,
            "message": "Data validated Successfully"
        }


class GetFoodPackageOnDay(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.ListFoodPackageSerializer

    def get_queryset(self):
        food_packages = food_package_models.FoodPackageMeal.objects.filter(
            meal__day=self.kwargs['day'], meal__food_type=self.kwargs['type'])
        return [food_package.food_package for food_package in food_packages]
