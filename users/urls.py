from django.urls import path,include
from .views import UsersViewset,AuthViewset
from rest_framework.routers import DefaultRouter


route = DefaultRouter()
route.register(r'users',UsersViewset,basename='users')
route.register(r'auth', AuthViewset, basename='auth')

urlpatterns = [
    path('',include(route.urls))
]
