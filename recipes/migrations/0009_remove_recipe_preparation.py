# Generated by Django 4.2.3 on 2023-07-19 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_preparation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='preparation',
        ),
    ]
