from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home_page_view_list"),
    path('recipe/<int:pk>/', views.recipe_detail, name="recipe_detail_page"),
    path('chefs/', views.chef, name="chef_page"),
    path('chef_profile/<int:pk>/', views.chef_profile, name="chef_profile_page"),
    path('category/<int:pk>/', views.category, name="category"),
    path('recipe/new/', views.recipe_new, name='recipe_new'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
