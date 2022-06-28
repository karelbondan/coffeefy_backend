# from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import CoffeeSerializer, SuggestionSerializer, UserSerializer
from .models import Coffee, Suggestions

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SuggestionsViewSet(viewsets.ModelViewSet):
    queryset = Suggestions.objects.all()
    serializer_class = SuggestionSerializer

class CoffeeViewSet(viewsets.ModelViewSet):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer