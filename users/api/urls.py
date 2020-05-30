from django.urls import path

from users.api.views import UserList, UserProfileRUAPIView

urlpatterns = [
    path("users/", UserList.as_view(), name='user-list'),
    path("users/<int:pk>/", UserProfileRUAPIView.as_view(), name='user-detail'),
]
