from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from market.models import MarketModel
User=get_user_model()
FLOOR=(
    ('first','first'),
    ('second',"second"),
    ('third','third'),
    ('fourth','fourth'),
    ('fifth','fifth'),
    ('sixth','sixth'),
    ('seventh','seventh'),
    ('eighth','eighth')
)

class shopModel(models.Model):
    name=models.CharField(max_length=150)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    market=models.ForeignKey(MarketModel,on_delete=models.CASCADE)
    floor=models.CharField(max_length=10,choices=FLOOR)
    contact_number=models.CharField(max_length=11)
    category=models.CharField(max_length=100,blank=True,null=True)

    # make unique name in a market
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'market'], name='unique_shop_name_in_market')
        ]
    def __str__(self):
        return self.name
     
    def save(self, *args, **kwargs):
      try: 
         if self.pk is not None:
           old_instance=shopModel.objects.get(pk=self.pk)
           if old_instance.owner != self.owner:
               if old_instance.owner.role != "Customer":
                      old_instance.owner.role="Customer"
                      old_instance.owner.save()
      except shopModel.DoesNotExist:
          pass  # New object, no old owner

      if self.owner.role!="ShopOwner":
           self.owner.role="ShopOwner"
           self.owner.save()

       
      super().save(*args, **kwargs)

    
 

        

    


# model for item /product 

CATEGORYS=(
    ('Man','Man'),
    ('Women','Women'),
    ('Kids','Kids'),
    ('Sport','Sport'),
    ('All','All'),
)
class ItemModel(models.Model):
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    shop=models.ForeignKey(shopModel,on_delete=models.CASCADE,related_name='items')
    name=models.CharField(max_length=140)
    price=models.CharField(max_length=40)
    discription=models.TextField(blank=True)
    category=models.CharField(max_length=20,choices=CATEGORYS)
    is_available=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
         ordering = ['-created_at']



    
    def __str__(self):
        return f"{self.name} ({self.shop.name})"
    