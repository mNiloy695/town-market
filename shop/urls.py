from django.urls import path,include
from rest_framework import routers
from .views import shopView,ItemView
router=routers.DefaultRouter()
router.register("list",shopView,basename='shop')
router.register('items',ItemView,basename="items")

urlpatterns = [
    path('',include(router.urls)),
]
