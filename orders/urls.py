from django.urls import path,include
from .views import OrdersViewset
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register(r'orders',OrdersViewset,basename='orders')

urlpatterns = [
    path('',include(route.urls))
]
