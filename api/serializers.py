from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Suggestions, Coffee

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = ['name', 'suggestion']

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Coffee
        fields = ['name', 'description', 'dateAdded', 'price']