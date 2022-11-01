from dataclasses import field
from rest_framework import serializers
from .models import hngapi

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=hngapi
        fields= ("__all__")