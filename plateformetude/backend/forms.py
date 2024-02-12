from django import forms
from .models import *

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'

class UserForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)





class ProfesseurForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = '__all__'  # Inclure tous les champs du modèle


class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        exclude = ['etudiants', 'professeurs']

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
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

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['full_name', 'message']


