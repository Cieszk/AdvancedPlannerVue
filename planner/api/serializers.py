from django.contrib.admin.widgets import AdminSplitDateTime

from rest_framework import serializers

from planner.models import Task, Ingredient, Recipe, GrocieresShoppingList

class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model"""
    class Meta:
        model = Task
        exclude = ('user',)

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredient model"""
    class Meta:
        model = Ingredient
        fields = '__all__'
    
class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe model"""
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = '__all__'

class GrocieresShoppingListSerializer(serializers.ModelSerializer):
    """Serializer for GroceriesShoppingList model"""
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = GrocieresShoppingList
        fields = '__all__'