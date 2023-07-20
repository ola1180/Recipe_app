from .models import Recipe, Chef, Category
from django.shortcuts import render, get_object_or_404


def home(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.all()
    return render(request, '../templates/recipes/home.html', {'recipes': recipes, 'categories': categories})


def recipe_detail(request, pk):
    categories = Category.objects.all()
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, '../templates/recipes/recipe_detail.html', {'recipe': recipe, 'categories': categories})


def chef(request):
    categories = Category.objects.all()
    chefs = Chef.objects.all()
    return render(request, '../templates/recipes/chef.html', {'chefs': chefs, 'categories': categories})


def chef_profile(request, pk):
    categories = Category.objects.all()
    chef = get_object_or_404(Chef, pk=pk)
    chef_recipes = Recipe.objects.filter(chef=pk)
    return render(request, '../templates/recipes/chef_profile.html',
                  {'chef': chef, 'chef_recipes': chef_recipes, 'categories': categories})


def category(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Recipe, pk=pk)
    category_recipes = Recipe.objects.filter(categories=pk)
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, '../templates/recipes/category_detail.html', {'category': category, 'categories': categories,'category_recipes': category_recipes, 'recipe': recipe})
