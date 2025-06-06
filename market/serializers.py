from .models import MarketModel
from rest_framework import serializers

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model=MarketModel
        fields=['name','location']

    