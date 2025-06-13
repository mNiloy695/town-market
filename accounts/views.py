from django.shortcuts import render,redirect
# Create your views here.
from rest_framework import viewsets
from  .serializers import RegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from rest_framework.response import Response

from  .models import User
from rest_framework import permissions

class isOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id
class RegistrationView(viewsets.ModelViewSet):
    serializer_class=RegistrationSerializer
    queryset=User.objects.all()

    def get_permissions(self):
        user=self.request.user
        #set permission for user
        if not user.is_authenticated:
            if self.request.method in ["GET","POST"]:
                return [permissions.AllowAny()]
            return [permissions.IsAuthenticated()]
        if user.is_authenticated and not user.is_staff:
            if self.request.method in ["GET","PUT","PATCH","DELETE"]:
                return  [isOwnerPermission()]
            return [permissions.IsAdminUser()]
        return [permissions.IsAdminUser()]
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            user=serializer.save()
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link=f'http://127.0.0.1:8000/account/active/{uid}/{token}/'
            subject="registration confirm mail"
            email_body=render_to_string('confirm_mail.html',{"confirm_link":confirm_link})
            email=EmailMultiAlternatives(subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response("check your mail")
        else:
            return Response(serializer.errors)

        
def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError,User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            return HttpResponse("Account varified")
        
    return HttpResponse("Invalid link")
           


   


