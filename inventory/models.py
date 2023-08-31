from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unitchoice=(
       ("tbsp","tablespoon"),
       ( "lbs","pounds"),
	   ( "g","grams"),
	   ( "ou","ounces"),
       ("eggs","eggs")
    )
    unit=models.CharField(max_length=5,choices=unitchoice, default="tbsp")

    def get_absolute_url(self):
       return "/ingredients"

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
  
    def get_absolute_url(self):
       return "/menuitems"   

    def __str__(self):
        return f"{self.title}"
 
class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
      
    def get_absolute_url(self):
       return "/reciperequirements"   

    def __str__(self):
        return f"{self.menu_item} - {self.ingredient}: {self.quantity}"

class Purchase(models.Model):
    purchase_date = models.DateTimeField(default=timezone.now)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
          
    def get_absolute_url(self):
       return "/purchases" 

    def __str__(self):
        return f"{self.purchase_date}: {self.quantity} x {self.menu_item}"
