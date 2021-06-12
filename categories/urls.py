  
from django.urls import path
from .views import CategoryViews

urlpatterns = [
    path('categories/create', CategoryViews.create, name='categories_create')
]