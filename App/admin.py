from django.contrib import admin
from .models import Professeur, Salle, Classe, EmploiDuTemps

@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Salle)
class SalleAdmin(admin.ModelAdmin):
    list_display = ('numero',)

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(EmploiDuTemps)
class EmploiDuTempsAdmin(admin.ModelAdmin):
    list_display = ('professeur', 'classe', 'salle', 'jour', 'heure_debut', 'heure_fin')
    list_filter = ('jour', 'professeur', 'classe', 'salle')
    search_fields = ('professeur__nom', 'classe__nom', 'salle__numero')
