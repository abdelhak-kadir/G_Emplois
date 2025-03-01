from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns = [
        path('', views.ajouter_emploi, name='ajouter_emploi'),

    path('liste/', views.liste_emplois, name='liste_emplois'),
    path('generer/', views.generer_emploi_view, name='generer_emploi'),
]
