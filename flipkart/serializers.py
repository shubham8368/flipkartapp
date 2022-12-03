from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from .models import Registration


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
