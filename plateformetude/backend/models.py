from django.db import models
from .enums import InscriptionStatus
import json

class Etudiant(models.Model):
    nom_Etud = models.CharField(max_length=30)
    prenom_Etud = models.CharField(max_length=30)
    email_Etud = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=100)
    date_Naissance = models.DateField()
    universite_Provenance = models.CharField(max_length=50)

class Cours(models.Model):
    nom_Cours = models.CharField(max_length=30, unique=True)
    libelle_Cours = models.CharField(max_length=50)
    contenue_text = models.TextField(null=True)  # Pour le texte
    urls_contenue = models.TextField(null=True)   # Pour les URLs stockées sous forme de JSON
    etudiants = models.ManyToManyField(Etudiant, related_name='cours')  # Relation many-to-many avec Etudiant
    professeurs = models.ManyToManyField('Professeur', related_name='cours')  # Relation many-to-many avec Professeur



class Inscription(models.Model):
    id_Etud = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    id_Cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    id_Session = models.IntegerField()
    date_Inscription = models.DateField()
    Status = models.CharField(max_length=50, choices=[(status.value, status.name) for status in InscriptionStatus])  # Utilisation de l'énumération pour les choix

class Professeur(models.Model):
    nom_Prof = models.CharField(max_length=30)
    prenom_Prof = models.CharField(max_length=30)
    email_Prof = models.EmailField(unique=True)
    password_Prof = models.CharField(max_length=100)

class Enseigner(models.Model):
    id_Prof = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    id_Cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    session_Debut = models.DateField()
    session_Fin = models.DateField()
    volume_Horaire = models.IntegerField()

class Module(models.Model):
    nom_Module = models.CharField(max_length=30)
    libelle_Module = models.CharField(max_length=50)
    cours = models.ManyToManyField(Cours, related_name='modules')  # Relation many-to-many avec Cours

class Contenir(models.Model):
    id_Cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    id_Module = models.ForeignKey(Module, on_delete=models.CASCADE)
