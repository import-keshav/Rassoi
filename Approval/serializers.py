from django import forms
from rest_framework import serializers

from . import models as approval_models
from Shop import serializers as shop_serializer

class GetGroceryApprovalSerializer(serializers.ModelSerializer):
    grocery = shop_serializer.ListGroceriesSerializer()
    class Meta:
        model = approval_models.GroceryApproval
        fields = '__all__'


class GetFruitApprovalSerializer(serializers.ModelSerializer):
    fruit = shop_serializer.ListFruitsSerializer()
    class Meta:
        model = approval_models.FruitApproval
        fields = '__all__'


class GetGVegetableApprovalSerializer(serializers.ModelSerializer):
    vegetable = shop_serializer.ListVegetableSerializer()
    class Meta:
        model = approval_models.VegetableApproval
        fields = '__all__'
