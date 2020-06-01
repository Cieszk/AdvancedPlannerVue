from django.urls import path

from planner.api import views as pv

urlpatterns = [
    path('tasks/', pv.TaskListAPIView.as_view({
        'get':'list', 
        'post': 'create'}), 
        name='task-list'
    ),
    path('tasks/<int:pk>/', pv.TaskRUDAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/done/', pv.TaskSetAsDoneAPIView.as_view(), name='task-set-done'),

    path('ingredients/', 
        pv.IngredientListCreateAPIViewSet.as_view({
        'get': 'list',
        'post': 'create'}),
        name='ingredient-list'
    ),

    path('recipes/', pv.RecipeListAPIView.as_view(), name='recipe-list'),
    path('recipes/create/', pv.RecipeCreateAPIView.as_view(), name='recipe-create'),
    path('recipes/<int:pk>/', pv.RecipeRUDAPIView.as_view(), name='recipe-detail')
]
