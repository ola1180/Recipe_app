from django.db import models


class Chef(models.Model):
    """
    Chef model

    Attributes:
        name (CharField)
        bio (TextField)
    """
    name = models.CharField(max_length=50)
    bio = models.TextField
