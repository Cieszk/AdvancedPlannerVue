from django.contrib import admin

from planner.models import Task, Ingredient, Recipe, GrocieresShoppingList

admin.site.register(Task)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(GrocieresShoppingList)
