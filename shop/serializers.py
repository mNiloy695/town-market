from rest_framework import serializers
from .models import shopModel,ItemModel

class shopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=shopModel
        fields="__all__"
class itemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemModel
        fields="__all__"

