from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home.as_view(),name = "home"),
    path('staffhome/', views.StaffHome.as_view(),name = "staffhome"),
    path("account/", include("django.contrib.auth.urls")),
    path("signup/", views.SignUp.as_view(),name = "signup"),
    path("logout/", views.logout_request,name = "logout"),
    path('ingredients/', views.IngredientList.as_view(),name = "ingredients"),
    path('ingredients/addingredient', views.AddIngredient.as_view(),name = "addingredient"),
    path('ingredients/<int:pk>/deleteingredient', views.DeleteIngredient.as_view(),name = "deleteingredient"),
    path('ingredients/<int:pk>/updateingredient', views.UpdateIngredient.as_view(),name = "updateingredient"),
    path('menuitems/', views.MenuItemList.as_view(),name = "menuitems"),
    path('menuitems/addmenuitems', views.AddMenuItem.as_view(),name = "addmenuitems"),
    path('menuitems/<int:pk>/deletemenuitems', views.DeleteMenuItem.as_view(),name = "deletemenuitems"),
    path('menuitems/<int:pk>/updatemenuitems', views.UpdateMenuItem.as_view(),name = "updatemenuitems"),
    path('purchases/', views.PurchaseList.as_view(),name = "purchases"),
    path('purchases/addpurchases', views.AddPurchase.as_view(),name = "addpurchases"),
    path('purchases/<int:pk>/deletepurchases', views.DeletePurchase.as_view(),name = "deletepurchases"),
    path('purchases/<int:pk>/updatepurchases', views.UpdatePurchase.as_view(),name = "updatepurchases"),
    path('reciperequirements/', views.RecipeRequirementsList.as_view(),name = "reciperequirements"),
    path('reciperequirements/addreciperequirements', views.AddRecipeRequirements.as_view(),name = "addreciperequirements"),
    path('reciperequirements/<int:pk>/deletereciperequirements', views.DeleteRecipeRequirements.as_view(),name = "deletereciperequirements"),
    path('reciperequirements/<int:pk>/updatereciperequirements', views.UpdateRecipeRequirements.as_view(),name = "updatereciperequirements"),
    path('profitrevenue/', views.profitrevenue_list,name = "profitrevenue"),
]
    
