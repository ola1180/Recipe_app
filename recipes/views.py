from .models import Recipe, Ingredient
from django.shortcuts import render, get_object_or_404


def home(request):
    recipes = Recipe.objects.all()
    return render(request, '../templates/recipes/home.html', {'recipes': recipes})



def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, '../templates/recipes/recipe_detail.html', {'recipe': recipe})


def chef(request):
    return render(request, '../templates/recipes/chef.html')


def category(request):
    return render(request, '../templates/recipes/category.html')
