# Generated by Django 4.2.3 on 2023-07-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(default='image', upload_to='files/banner'),
        ),
    ]
