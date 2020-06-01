from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action

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
        return Task.objects.all().filter(user=current_user, done=False)

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


class IngredientListCreateAPIViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        current_user = self.request.user
        return Ingredient.objects.all()
    
    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)

class RecipeListAPIView(generics.ListAPIView):
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Recipe.objects.all()

class RecipeCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(user=author)
    
class RecipeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer

    def get_queryset(self):
        current_user = self.request.user
        return Recipe.objects.all().filter(user=current_user)

class GroceriesShoppingListCreateAPIViewSet(viewsets.ModelViewSet):
    serializer_class = GrocieresShoppingListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        current_user = self.request.user
        return GrocieresShoppingList.objects.all().filter(user=current_user, active=True)

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)

class GroceriesRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GrocieresShoppingListSerializer

    def get_queryset(self):
        current_user = self.request.user
        return GrocieresShoppingList.objects.all().filter(user=current_user)
