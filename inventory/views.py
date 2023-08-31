from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import Ingredient,RecipeRequirements,MenuItem,Purchase

# Create your views here.
class IngredientList(ListView):
    model = Ingredient
    template = "inventory/ingredient_list.html"
