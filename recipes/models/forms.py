from django import forms
from . import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'ingredients', 'preparation', 'photo',)
