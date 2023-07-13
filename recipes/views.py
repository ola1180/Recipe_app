from django.shortcuts import render


def home(request):
    return render(request, '../templates/recipes/home.html')


def recipe_detail(request):
    return render(request, '../templates/recipes/recipe_detail.html')


def chef(request):
    return render(request, '../templates/recipes/chef.html')


def category(request):
    return render(request, '../templates/recipes/category.html')
