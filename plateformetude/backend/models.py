from django.db import models
from .enums import InscriptionStatuts
from django.core.exceptions import ValidationError
from .enums import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from django.contrib.auth.hashers import make_password
from django.utils import timezone



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
    modules= models.ManyToManyField('Module', related_name='modules_cours')
    # etudiants = models.ManyToManyField(Etudiant, related_name='cours')
    # professeurs = models.ManyToManyField(Professeur, related_name='cours')
    def get_urls(self):
        return [url.strip() for url in self.urls.split() if url.strip()]
    def __str__(self):
        return f"{self.titre}"

class Module(models.Model):
    nom = models.CharField(max_length=20)
    libelle = models.CharField(max_length=30)
    cours = models.ManyToManyField(Cours, related_name='cours_modules')
    def __str__(self):
        return f"{self.nom}"




class Enseigner(models.Model):
    id_Session = models.IntegerField()
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    session_Debut = models.DateField()
    session_Fin = models.DateField()
    volume_Horaire = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(60)])


class Inscription(models.Model):
    id_Session = models.IntegerField()
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    date_Inscription = models.DateField(default=timezone.now)
    status = models.CharField(choices=InscriptionStatuts.choices,max_length=25,default=InscriptionStatuts.EN_COURS)


# class Contenir(models.Model):
#     id_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
#     id_module = models.ForeignKey(Module, on_delete=models.CASCADE)


class Feedback(models.Model):
    full_name = models.CharField(default="Anonyme",null=True,max_length=50)
    message = models.TextField()
    def __str__(self):
        return f"{self.full_name}"



