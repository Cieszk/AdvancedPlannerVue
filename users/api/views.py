from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import CustomUser
from users.api.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
