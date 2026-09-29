from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='games_inicio'),
    path('catalogo/', views.catalogo, name='games_catalogo'),
]
