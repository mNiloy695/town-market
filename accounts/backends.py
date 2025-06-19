from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class PhoneBackend(ModelBackend):
    def authenticate(self, request, phone=None, password=None, **kwargs):
        UserModel = get_user_model()

        if phone is None:
            phone = kwargs.get('phone')

        if phone and password:
            try:
                user = UserModel.objects.get(phone=phone)
                if user.check_password(password):
                    return user
            except UserModel.DoesNotExist:
                return None

        return None
