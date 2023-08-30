from .serializer import Orders, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

class OrdersViewset(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get','post']
    
    def get_queryset(self):
        return Orders.objects.filter(owner=self.request.user)
    