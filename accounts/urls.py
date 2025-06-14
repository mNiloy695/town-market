from .views import RegistrationView,activate,LoginView,UserLogoutViewSet
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('register',RegistrationView,basename="register")
urlpatterns = [
    path('',include(router.urls)),
    path('active/<uid64>/<token>/',activate,name='activate'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',UserLogoutViewSet.as_view(),name='logout'),

]

