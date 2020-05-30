from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import CustomUser, UserProfile
from users.api.serializers import UserSerializer, UserProfileSerializer
from users.api.permissions import IsAccountOwnerOrReadOnly

class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer

class UserProfileRUAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, IsAccountOwnerOrReadOnly)

    def get_queryset(self):
        if self.kwargs['pk']:
            return UserProfile.objects.filter(user_id=self.kwargs['pk']).order_by('pk')
        else:
            return UserProfile.objects.all().order_by('pk')