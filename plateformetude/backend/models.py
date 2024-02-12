from django.db import models
from .enums import InscriptionStatuts
from django.core.exceptions import ValidationError
from .enums import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from django.contrib.auth.hashers import make_password



class Utilisateur(models.Model):
    nom=models.CharField(max_length=50,)
    prenom=models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length=254)
    password=models.CharField(max_length=100,null=True)
    date_naissance = models.DateField(null=True)
    REQUIRED_FIELDS = ['nom', 'prenom', 'email','password']

    class Meta:
        abstract=True
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    def set_password(self,rawpassword):
        self.password=make_password(rawpassword)
    def verify_password(self,entrypassword):
        if self.password==entrypassword :return True
        else:return False


class Etudiant(Utilisateur):
    universite_provenance =models.CharField(choices=Universite.choices,max_length=10)

class Professeur(Utilisateur):
    pass

class Cours(models.Model):
    titre = models.CharField(max_length=30, unique=True)
    libelle = models.CharField(max_length=50,null=True)
    contenue_texte = models.TextField(null=True)
    urls = models.TextField(null=True)
    etudiants = models.ManyToManyField(Etudiant, related_name='cours')
    professeurs = models.ManyToManyField(Professeur, related_name='cours')
    def get_urls_list(self):
        return [url.strip() for url in self.urls.split(',') if url.strip()]
    def __str__(self):
        return f"{self.nom}"


class Inscription(models.Model):
    id_Session = models.IntegerField()
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    id_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    date_Inscription = models.DateField()
    status = models.CharField(choices=InscriptionStatuts.choices,max_length=25,default=InscriptionStatuts.EN_COURS)



class Enseigner(models.Model):
    id_professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
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
    cours = models.ManyToManyField(Cours, related_name='modules')
    def __str__(self):
        return f"{self.nom}"

class Contenir(models.Model):
    id_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    id_module = models.ForeignKey(Module, on_delete=models.CASCADE)


class Feedback(models.Model):
    full_name = models.CharField(default="Anonyme",null=True,max_length=50)
    message = models.TextField()
    def __str__(self):
        return f"{self.full_name}"


