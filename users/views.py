from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializer import UserSerializer, LoginSerializer
from .models import User
from .utils import user_exists,fetch_user

class UsersViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get','post','delete']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                'user': serializer.data,
                'token': token.key
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )



class AuthViewset(ModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username= serializer.validated_data['username']
        user = user_exists(username)
        password=serializer.validated_data['password']
        
       
        if not user:
            return Response({"username": 'User does not exist'},status=status.HTTP_404_NOT_FOUND)

        elif not fetch_user(username,password):
            return Response({"password": 'Incorrect Password'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            token, created = Token.objects.get_or_create(user=fetch_user(username,password))
            return Response({'token': token.key})
        