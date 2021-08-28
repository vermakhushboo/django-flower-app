from rest_framework import serializers
from .models import Flower

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower #model to be serialized
        fields = ('flower_name', 'flower_color')