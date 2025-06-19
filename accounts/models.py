from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
TYPE=(
    ('Customer','Customer'),
    ('ShopOwner','ShopOwner'),
)
class User(AbstractUser):
    profile_img=models.ImageField(upload_to='user_profile/',blank=True,null=True)
    phone=models.CharField(max_length=11,unique=True)
    role=models.CharField(max_length=20,default="Customer",choices=TYPE)
    def __str__(self):
        return f'{self.username}  {self.phone}'
    # USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = ['phone']