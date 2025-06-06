from .views import MarketView
from rest_framework import routers
from django.urls import include,path
router=routers.DefaultRouter()

router.register('list',MarketView,basename='market')

urlpatterns = [
    path("",include(router.urls))
]
