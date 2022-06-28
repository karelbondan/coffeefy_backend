from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import CoffeeViewSet, SuggestionsViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('suggestions', SuggestionsViewSet)
router.register('coffee', CoffeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
