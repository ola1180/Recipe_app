from django.db import models


class Chef(models.Model):
    """
    Chef model

    Attributes:
        name (CharField)
        bio (TextField)
        profile_photo (ImageField)
    """
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='images', default='user.png')

