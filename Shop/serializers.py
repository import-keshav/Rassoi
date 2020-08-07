from django import forms
from rest_framework import serializers

from . import models as shop_models


class ListShop(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Shop
        fields = '__all__'


class ListSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Slots
        fields = '__all__'


class CreateSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Slots
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'category', 'start_time', 'end_time', 'date']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data

class UpdateDeleteSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Slots
        fields = '__all__'
