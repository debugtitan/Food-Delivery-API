from rest_framework.serializers import ModelSerializer
from .models import Cart


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['product','quantity','total']
        
        def total(self, instance):
            total = sum(item.quantity for item in instance.cart_items.all())
            return total