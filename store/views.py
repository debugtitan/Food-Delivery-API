from rest_framework.viewsets import ModelViewSet
from .serializer import FoodItem,Categories,FoodItemsSerializer,CategorySerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication


class CategoryViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    authentication_classes =[TokenAuthentication]
    
    
class FoodItemViewset(ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class  = FoodItemsSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]