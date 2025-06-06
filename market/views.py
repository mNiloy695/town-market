from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from .serializers import MarketSerializer
from .models import MarketModel
class MarketView(viewsets.ModelViewSet):
    serializer_class=MarketSerializer
    queryset=MarketModel.objects.all()
    def get_permissions(self):
        user=self.request.user
        print("checking user using self.request.user: ",user)
        
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        else:
             return [permissions.IsAdminUser()]
        
        