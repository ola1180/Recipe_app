from django.contrib import admin
from .models import Category, Chef, Ingredient, Recipe


# Register your models here.


admin.site.register(Category)
admin.site.register(Chef)
admin.site.register(Ingredient)
admin.site.register(Recipe,)
