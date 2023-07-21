from django.contrib import admin
from .models import Category, Chef, Ingredient, Recipe, Profile


# Register your models here.


admin.site.register(Category)
admin.site.register(Chef)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Profile)

