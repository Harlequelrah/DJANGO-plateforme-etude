from django import forms
from .models import Etudiant, Cours, Inscription, Professeur, Enseigner, Module, Contenir

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'  # Inclure tous les champs du modèle

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        exclude = ['etudiants', 'professeurs']  # Exclure les champs many-to-many

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'  # Inclure tous les champs du modèle

class ProfesseurForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = '__all__'  # Inclure tous les champs du modèle

class EnseignerForm(forms.ModelForm):
    class Meta:
        model = Enseigner
        fields = '__all__'  # Inclure tous les champs du modèle

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = '__all__'  # Inclure tous les champs du modèle

class ContenirForm(forms.ModelForm):
    class Meta:
        model = Contenir
        fields = '__all__'  # Inclure tous les champs du modèle
