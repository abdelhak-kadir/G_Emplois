from django.shortcuts import render, redirect
from .models import *
from datetime import time
from .form import *

def generer_emploi():
    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    heures = [time(8, 0), time(10, 0), time(12, 0), time(14, 0), time(16, 0)]
    
    # Supprimer les anciens emplois du temps
    EmploiDuTemps.objects.all().delete()
    
    salles_disponibles = list(Salle.objects.all())
    
    for jour in jours:
        for heure in heures:
            for professeur in Professeur.objects.all():
                # Récupérer les classes du professeur
                classes = professeur.classes.all()
                for classe in classes:
                    # Vérifier qu'il y a encore des salles disponibles
                    if not salles_disponibles:
                        break
                    
                    salle = salles_disponibles.pop(0)  # Prendre une salle disponible
                    
                    # Vérifier qu'il n'y a pas de conflit d'horaire
                    conflit_prof = EmploiDuTemps.objects.filter(
                        professeur=professeur, jour=jour, heure_debut=heure
                    ).exists()
                    
                    conflit_classe = EmploiDuTemps.objects.filter(
                        classe=classe, jour=jour, heure_debut=heure
                    ).exists()
                    
                    if not conflit_prof and not conflit_classe:
                        EmploiDuTemps.objects.create(
                            professeur=professeur,
                            classe=classe,
                            salle=salle,
                            jour=jour,
                            heure_debut=heure,
                            heure_fin=time(heure.hour + 2, 0)  # Chaque cours dure 2h
                        )

def generer_emploi_view(request):
    generer_emploi()
    return redirect('liste_emplois')

def liste_emplois(request):
    emplois = EmploiDuTemps.objects.all()
    professeurs = Professeur.objects.all()
    salles = Salle.objects.all()
    classes = Classe.objects.all()
    return render(request, 'liste_emplois.html', {
        'emplois': emplois,
        'professeurs': professeurs,
        'salles': salles,
        'classes': classes
    })

def ajouter_emploi(request):
    if request.method == "POST":
        form = EmploiDuTempsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_emplois')
    else:
        form = EmploiDuTempsForm()
    return render(request, 'ajouter_emploi.html', {'form': form})