from django import forms
from .models import Ingredient, MenuItem, Purchase, RecipeRequirements

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"

class RecipeRequirementsForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = "__all__"