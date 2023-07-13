from django.db import models


class Category(models.Model):
    """
    Category model

    Attributes:
        name (CharField)

    """

    name = models.CharField(max_length=50)
