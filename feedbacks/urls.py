from django.urls import path,include
from .views import DeliveryFeedbackViewSet
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register(r'feedbacks',DeliveryFeedbackViewSet,basename='rate')

urlpatterns = [
    path('',include(route.urls))
]
