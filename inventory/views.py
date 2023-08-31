from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView
from .models import Ingredient,MenuItem,Purchase,RecipeRequirements
from django.db.models import Sum
from .forms import IngredientForm, MenuItemForm, PurchaseForm, RecipeRequirementsForm
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

class Home(ListView):
    model = MenuItem
    template_name = "inventory/home.html"
    form_class = MenuItemForm

class StaffHome(LoginRequiredMixin,TemplateView):
    template_name = "inventory/staffhome.html"

class SignUp(CreateView):
    template_name = "registration/signup.html"
    success_url=reverse_lazy("login")
    form_class = UserCreationForm

def logout_request(request):
    logout(request)
    return redirect("home")

class IngredientList(LoginRequiredMixin,ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class AddIngredient(LoginRequiredMixin,CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm

class UpdateIngredient(LoginRequiredMixin,UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientForm

class DeleteIngredient(LoginRequiredMixin,DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = "/ingredients"

class MenuItemList(LoginRequiredMixin,ListView):
    model = MenuItem
    template_name = "inventory/menuitem_list.html"

class AddMenuItem(LoginRequiredMixin,CreateView):
    model = MenuItem
    template_name = "inventory/add_menuitem.html"
    form_class = MenuItemForm

class UpdateMenuItem(LoginRequiredMixin,UpdateView):
    model = MenuItem
    template_name = "inventory/update_menuitem.html"
    form_class = MenuItemForm

class DeleteMenuItem(LoginRequiredMixin,DeleteView):
    model = MenuItem
    template_name = "inventory/delete_menuitem.html"
    success_url = "/menuitems"

class PurchaseList(LoginRequiredMixin,ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"

class AddPurchase(LoginRequiredMixin,CreateView):
    model = Purchase
    template_name = "inventory/add_purchase.html"
    form_class = PurchaseForm

class UpdatePurchase(LoginRequiredMixin,UpdateView):
    model = Purchase
    template_name = "inventory/update_purchase.html"
    form_class = PurchaseForm

class DeletePurchase(LoginRequiredMixin,DeleteView):
    model = Purchase
    template_name = "inventory/delete_purchase.html"
    success_url = "/purchases"

class RecipeRequirementsList(LoginRequiredMixin,ListView):
    model = RecipeRequirements
    template_name = "inventory/reciperequirements_list.html"

class AddRecipeRequirements(LoginRequiredMixin,CreateView):
    model = RecipeRequirements
    template_name = "inventory/add_reciperequirements.html"
    form_class = RecipeRequirementsForm

class UpdateRecipeRequirements(LoginRequiredMixin,UpdateView):
    model = RecipeRequirements
    template_name = "inventory/update_reciperequirements.html"
    form_class = RecipeRequirementsForm

class DeleteRecipeRequirements(LoginRequiredMixin,DeleteView):
    model = RecipeRequirements
    template_name = "inventory/delete_reciperequirements.html"
    success_url = "/reciperequirements"

@login_required
def calculate_profit_and_revenue(purchases, menu_items):
    revenue = sum(purchase.quantity * purchase.menu_item.price for purchase in purchases)
    total_cost = sum(requirement.ingredient.unit_price * requirement.quantity for requirement in RecipeRequirements.objects.all())
    profit = revenue - total_cost
    return revenue, profit

@login_required
def profitrevenue_list(request):
    menu_items = MenuItem.objects.all()
    purchases = Purchase.objects.all()

    revenue, profit = calculate_profit_and_revenue(purchases, menu_items)

    context = {
        'revenue': revenue,
        'profit': profit,
    }
    return render(request, 'inventory/profitrevenue_list.html', context)

