from django.urls import path
from .views import index, reset_cities

urlpatterns = [
    path('', index, name='index'),
    path('reset/', reset_cities, name='reset_cities'),
]