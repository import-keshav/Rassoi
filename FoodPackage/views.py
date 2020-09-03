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


class ListShopFoodPackage(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.ListFoodPackageSerializer

    def get_queryset(self):
        return food_package_models.FoodPackage.objects.filter(shop__pk=self.kwargs['pk'])


class UpdateDeleteFoodPackage(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.UpdateDeleteFoodPackageSerializer
    queryset = food_package_models.FoodPackage.objects.all()


class UpdateDeleteFoodPackageMeal(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.UpdateDeleteFoodPackageMealSerializer
    queryset = food_package_models.FoodPackageMeal.objects.all()


# class CreateFoodPackage(generics.CreateAPIView):
#     renderer_classes = [JSONRenderer]
#     serializer_class = food_package_serializer.CreateFoodPackageSerializer


class CreateFoodPackageMeal(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.CreateFoodPackageMealSerializer


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
                        "food_meal": food_meal
                })
                if food_package_meal_serializer_obj.is_valid():
                    food_package_meal_serializer_obj.save()
            return Response({
                'message': 'Food Package created Successfully',
                "id": food_package_serializer_obj.data['id']
            },)
        else:
            return Response(
                food_package_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


    def is_food_meal_valid(self, food_meals, food_package):
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
