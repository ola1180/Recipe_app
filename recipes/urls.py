from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home_page_view_list"),
    path('recipe/<int:pk>/', views.recipe_detail, name="recipe_detail_page"),
    path('chefs/', views.chef, name="chef_page"),
    path('categories/', views.category, name="category_page"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
