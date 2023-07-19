from django.db import models


class Ingredient(models.Model):
    """
    Ingredient model

    Attributes:
        name (CharField)
        quantity (CharField)

    """

    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.quantity}'

