from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page_view_list"),
    path('recipes/', views.recipe_detail, name="recipe_detail_page"),
    path('chefs/', views.chef, name="chef_page"),
    path('categories/', views.category, name="category_page"),

]
