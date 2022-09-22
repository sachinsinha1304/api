from dataclasses import fields
from rest_framework import serializers
from .models import Biddings, item,userDetails,SoldItems

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = userDetails
        fields = '__all__'

class biddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biddings
        fields = '__all__'

class soldItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldItems
        fields = '__all__'