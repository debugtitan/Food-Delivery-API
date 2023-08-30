from rest_framework.serializers import ModelSerializer
from .models import FoodItem,Categories

class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Categories
        fields  = ['name']
        

class FoodItemsSerializer(ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['category','item_name','item_image','item_price']