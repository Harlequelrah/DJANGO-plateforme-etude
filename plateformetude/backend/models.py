from django.db import models
from .enums import InscriptionStatus
from django.core.exceptions import ValidationError
from enums import *
from django.core.validators import MaxValueValidator, MinValueValidator


class Utilisateur(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length=254)
    date_naissance = models.DateField(null=True)
    class Meta:
        abstract=True
    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Etudiant(Utilisateur):
    universite_provenance =models.CharField(choices=Universite.choices,max_length=10)
class Professeur(Utilisateur):
    pass

class Cours(models.Model):
    titre = models.CharField(max_length=30, unique=True)
    libelle = models.CharField(max_length=50,null=True)
    contenue_texte = models.TextField(null=True)  # Pour le texte
    urls = models.TextField(null=True)   # Pour les URLs stockées sous forme de JSON
    etudiants = models.ManyToManyField(Etudiant, related_name='cours')  #Relation many-to-many avec Etudiant
    professeurs = models.ManyToManyField(Professeur, related_name='cours')  # Relation many-to-many avec Professeur
    def get_urls_list(self):
        return [url.strip() for url in self.urls.split(',') if url.strip()]


class Inscription(models.Model):
    # id_Session = models.IntegerField()
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    id_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    date_Inscription = models.DateField()
    status = models.CharField(max_length=50,choices=InscriptionStatuts.choices,max_length=25,default=InscriptionStatuts.EN_COURS)  # Utilisation de l'énumération pour les choix



class Enseigner(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    id_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    session_Debut = models.DateField()
    session_Fin = models.DateField()
    volume_Horaire = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(60)])
    def clean(self):
        super().clean()
        if self.session_Debut and self.session_Fin and self.session_Debut >= self.session_Fin:
            raise ValidationError("La date de début de session doit être antérieure à la date de fin de session.")

class Module(models.Model):
    nom = models.CharField(max_length=20)
    libelle = models.CharField(max_length=30)
    cours = models.ManyToManyField(Cours, related_name='modules')  # Relation many-to-many avec Cours

class Contenir(models.Model):
    id_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    id_module = models.ForeignKey(Module, on_delete=models.CASCADE)
