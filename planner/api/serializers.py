from django.contrib.admin.widgets import AdminSplitDateTime

from rest_framework import serializers

from planner.models import (
    Task, 
    Ingredient, 
    Recipe, 
    GrocieresShoppingList
)

class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model"""
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['done', 'user']

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredient model"""
    class Meta:
        model = Ingredient
        fields = '__all__'
        read_only_fields = ['active', 'user']
    
class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe model"""
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all())
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ['author']

class GrocieresShoppingListSerializer(serializers.ModelSerializer):
    """Serializer for GroceriesShoppingList model"""
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all())
    class Meta:
        model = GrocieresShoppingList
        exclude = ['user', 'active']