from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel=get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(write_only=True)
    class Meta:
        model=UserModel
        fields=['id','username','email','phone','password','first_name','last_name','role','profile_img','confirm_password']

    def save(self, **kwargs):
        username=self.validated_data['username']
        email=self.validated_data['email']
        phone=self.validated_data['phone']
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']
        role=self.validated_data['role']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        profile_image=self.validated_data['profile_img']

        if password !=confirm_password:
            raise serializers.ValidationError({'error':"your password and confrim password doesn't match ! "})
        if UserModel.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error':"The usename already exist "})
        if UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error":"The email already exist !"})
        
        accout=UserModel(username=username,email=email,first_name=first_name,last_name=last_name,profile_img=profile_image,phone=phone,role=role)
        accout.set_password(password)
        accout.is_active=False
        accout.save()
        return accout

