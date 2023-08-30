from rest_framework.serializers import ModelSerializer,Serializer,CharField
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'address', 'phone_number', 'gender', 'dob']



class LoginSerializer(Serializer):
    username = CharField()
    password = CharField()
    class Meta:
        fields = ['username','password']