from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

from planner.models import (
    Recipe, 
    Ingredient, 
    Task, 
    GrocieresShoppingList
)
from planner.api.serializers import (
    GrocieresShoppingListSerializer,
    IngredientSerializer,
    RecipeSerializer,
    TaskSerializer
)
from api_utils.permissions import IsAccountOwnerOrDenyAccess, IsAdminOrDenyAccess


class TaskListAPIView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsAccountOwnerOrDenyAccess)

    def get_queryset(self):
        current_user = self.request.user
        return Task.objects.all().filter(user=current_user)

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)

class TaskRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsAccountOwnerOrDenyAccess)

    def get_queryset(self):
        current_user = self.request.user
        return Task.objects.all().filter(user=current_user)

class TaskSetAsDoneAPIView(APIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsAccountOwnerOrDenyAccess)

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        current_user = request.user

        task.done = True
        task.save()

        serializer_context = {'request': request}
        serializer = self.serializer_class(task, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)