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
        photo (ImageField)
    """

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    preparation = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='images', default='user.png')
