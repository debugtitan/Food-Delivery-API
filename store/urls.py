from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FoodItemViewset,CategoryViewSet

route = DefaultRouter()
route.register(r'category',CategoryViewSet,basename='categories')
route.register(r'item',FoodItemViewset,basename='food_item')

urlpatterns = [
    path('products/',include(route.urls))
    
]
