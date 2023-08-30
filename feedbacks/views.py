from rest_framework import viewsets, permissions,authentication
from .models import DeliveryFeedback
from .serializer import DeliveryFeedbackSerializer
from orders.models import Orders
from rest_framework.response import Response

class IsOrderMakerOrAuthenticated(permissions.BasePermission):
    """
    Custom permission to only allow users who have made an order to give feedback,
    while allowing all authenticated users to view feedback.
    """
    def has_permission(self, request, view):
        if view.action == 'create':
            user_orders = Orders.objects.filter(owner=request.user)
            return user_orders.exists()
        return request.user and request.user.is_authenticated

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to delete feedback.
    """
    def has_permission(self, request, view):
        if view.action == 'destroy':
            return request.user and request.user.is_staff
        return True

class DeliveryFeedbackViewSet(viewsets.ModelViewSet):
    queryset = DeliveryFeedback.objects.all()
    serializer_class = DeliveryFeedbackSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def get_permissions(self):
        try:
            if self.action == 'create':
                permission_classes = [IsOrderMakerOrAuthenticated]
            elif self.action == 'destroy':
                permission_classes = [IsAdminOrReadOnly]
            else:
                permission_classes = [permissions.AllowAny]
            return [permission() for permission in permission_classes]
        
        except Exception as e:
            print(e)
            return Response({
                "message": e
            })
            
