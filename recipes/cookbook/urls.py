from django.contrib import admin
from django.urls import path, include

from .views import home_view, recipe_view

urlpatterns = [
    path('', home_view, name='home'),
    path('recipes/', home_view, name='home'),
    path('recipes/<recipe_name>/', recipe_view, name='calculate_recipe'),
    path('admin/', admin.site.urls),
]
