from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class PhoneBackend(ModelBackend):


    # set phone number as a login parameter
    def authenticate(self, request, phone=None, password=None, **kwargs):
        UserModel = get_user_model()
        u=UserModel.objects.get(phone=phone)
        print("The user is : ",UserModel.objects.get(phone=phone))
        user = None
        if phone is None:
            phone = kwargs.get('phone')
        if phone and password:
            try:
                user = UserModel.objects.get(phone=phone)
                
            except UserModel.DoesNotExist:
                return None
            if user.check_password(password):
                return user
        return None
