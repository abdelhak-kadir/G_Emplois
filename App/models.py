from django.db import models

JOURS_CHOICES = [
    ('Lundi', 'Lundi'),
    ('Mardi', 'Mardi'),
    ('Mercredi', 'Mercredi'),
    ('Jeudi', 'Jeudi'),
    ('Vendredi', 'Vendredi'),
    ('Samedi', 'Samedi')
]

class Professeur(models.Model):
    nom = models.CharField(max_length=100)
    classes = models.ManyToManyField('Classe', related_name="professeurs")

    def __str__(self):
        return self.nom

class Salle(models.Model):
    numero = models.CharField(max_length=10)

    def __str__(self):
        return f"Salle {self.numero}"

class Classe(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class EmploiDuTemps(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    jour = models.CharField(max_length=20, choices=JOURS_CHOICES)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return f"{self.professeur} - {self.classe} - {self.salle} ({self.jour} {self.heure_debut}-{self.heure_fin})"
