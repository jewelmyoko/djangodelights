from django.urls import path
from . import views

urlpatterns = [
    path('ingredients/', views.IngredientList.as_view(),name = "ingredients"),
]
