from django.db import models

from users.models import CustomUser

class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class IngredientDetail(models.Model):
    UNITS = (
        ('G', 'gram'),
        ('L', 'liter'),
        ('KG', 'kilogram'),
        ('DG', 'ounce'),
        ('TPS', 'teaspoon'),
        ('TBS', 'tablespoon'),
        ('GL', 'glass'),
        ('PCS', 'pieces')
    )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(
            blank=True, 
            null=True, 
            max_digits=5, 
            decimal_places=2
        )
    unit = models.CharField(
            max_length=3, 
            blank=True, 
            null=True, 
            choices=UNITS, 
            default=[0][0]
        )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(blank=True)
    prep_time = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ingredients = models.ForeignKey(IngredientDetail, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} - by {self.author}'


class GrocieresShoppingList(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    ingredients = models.ForeignKey(IngredientDetail, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
