from django.db import models

from . import Chef, Ingredient, Category


class Recipe(models.Model):
    """
    Recipe model

    Attributes:
        title (CharField)
        description (CharField)
        chef (ForeignKey)
        ingredients (ManyToManyField)
        categories (ManyToManyField)
    """

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
