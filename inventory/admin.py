from django.contrib import admin
from .models import MenuItem, Purchase, Ingredient, RecipeRequirements

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Purchase)
admin.site.register(RecipeRequirements)