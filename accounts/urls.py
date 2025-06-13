from .views import RegistrationView,activate
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('register',RegistrationView,basename="register")
urlpatterns = [
    path('',include(router.urls)),
    path('active/<uid64>/<token>/',activate,name='activate'),
]

