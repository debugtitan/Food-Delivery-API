import logging
from .serializer import Cart,CartSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from store.models import FoodItem

logger = logging.getLogger(__name__)


class CartViewset(ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user)
    
    @action(detail=False,methods=['POST'])
    def add_cart(self,request):
        try:
            product_id = request.data.get('product')
            quantity = request.data.get('quantity',1)
            product = FoodItem.objects.get(pk=product_id)
            cart_item, created = Cart.objects.get_or_create(
                owner=request.user,product=product
            )
        
            if not created:
                cart_item.quantity += int(quantity)
                cart_item.update_current_item_price()
                cart_item.save()
            serializer = self.get_serializer(cart_item)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f'An error occured {e}')
            return Response({
                "message": f"An error occurred while processing your request  - {e}",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR
            })
    
    @action(detail=True,methods=['POST'])
    def increase_quantity(self,request,pk=None):
        try:
            cart_item = self.get_object()
            cart_item.quantity  += 1
            cart_item.update_current_item_price()
            serializer = self.get_serializer(cart_item)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f'An error occured {e}')
            return Response({
                "message": f"An error occurred while processing your request  - {e}",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR
            })
    
    @action(detail=True,methods=['POST'])
    def decrease_quantity(self,request,pk=None):
        try:
            cart_item = self.get_object()
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.update_current_item_price()
                serializer = self.get_serializer(cart_item)
                return Response(serializer.data)
            else:
                return Response({
                    "message": 'Minimum quantity reached'
                })
        except Exception as e:
            logger.error(f'An error occured {e}')
            return Response({
                "message": f"An error occurred while processing your request  - {e}",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR
            })
    
    @action(detail=True,methods=['POST'])
    def delete_cart_item(self,request,pk=None):
        try:
            cart_item = self.get_object()
            cart_item.delete()
            return Response({
                "message": "Item deleted successfully!"
            })
        except Exception as e:
            logger.error(f'An error occured {e}')
            return Response({
                "message": f"An error occurred while processing your request  - {e}",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR
            })
    
    