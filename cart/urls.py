from django.urls import path,include
from .views  import CartViewset
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register(r'cart',CartViewset,basename='cart')

urlpatterns = [
    path('',include(route.urls))
]
