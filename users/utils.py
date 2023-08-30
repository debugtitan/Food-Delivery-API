import re
from .models import User
from django.contrib.auth import authenticate


def user_exists(user):
    if re.match(r"[^@]+@[^@]+\.[^@]+", user):
        return User.objects.filter(email=user).exists()
    else:
        return User.objects.filter(username=user).exists()


def fetch_user(username,password):
    user = None 
    if re.match(r"[^@]+@[^@]+\.[^@]+", username):
        user = authenticate(email=username, password=password)
    else:
        user = authenticate(username=username, password=password)
    #print(user)
    return user
