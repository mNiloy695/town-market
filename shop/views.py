from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
# Create your views here.
from .serializers import shopModelSerializer,itemModelSerializer
from .models import shopModel,ItemModel
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend

class shopView(viewsets.ModelViewSet):
    serializer_class=shopModelSerializer
    queryset=shopModel.objects.all()
    filter_backends=[SearchFilter]
    search_fields=['market__id','name']

    # # set permisson
    # only admin can do all operation
    # user can see the shop 

    def get_permissions(self):
        
        if self.request.method =='GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]

# item view

# custom permission set for woner of the shop

class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.shop.owner==request.user
        
class ItemView(viewsets.ModelViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = itemModelSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_fields = ['shop']
    search_fields=['name','discription','category']

    def get_permissions(self):
        # Anyone can read (GET)
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        
        # Admins can do anything
        if self.request.user.is_staff:
            return [permissions.IsAdminUser()]
        
        # Non-admin users must be the owner
        return [IsOwnerPermission()]

    def perform_create(self, serializer):
        shop = serializer.validated_data.get('shop')
        if  shop.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("You are not the owner of this shop.")
        serializer.save()
    







