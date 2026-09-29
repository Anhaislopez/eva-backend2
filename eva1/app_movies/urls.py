from django.urls import path

from . import views

urlpatterns = [
    path('', views.cartelera, name='movies_cartelera'),
    path('estrenos/', views.estrenos, name='movies_estrenos'),
]
