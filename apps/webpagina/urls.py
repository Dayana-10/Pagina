
from django.urls import path
from .views import home

urlpatterns = [
    path('paginaprincipal/', home, name='Binevenido'),
]
