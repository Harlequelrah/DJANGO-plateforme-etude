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
        # fields="__all__"
        # exclude = ['etudiants', 'professeurs']
        exclude = ['modules']

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = '__all__'  # Inclure tous les champs du modèle

class EnseignerUpdate(forms.Form):
    # class Meta:
    #     model= Enseigner
    titre = forms.CharField(max_length=30, required=False)
    libelle = forms.CharField(max_length=50, required=False)
    contenue_texte = forms.CharField(widget=forms.Textarea, required=False)
    urls = forms.CharField(widget=forms.Textarea, required=False)
    session_Debut = forms.DateField(required=False)
    session_Fin = forms.DateField(required=False)
    volume_Horaire = forms.IntegerField(required=False, validators=[MinValueValidator(0), MaxValueValidator(60)])
    id_Session = forms.IntegerField(required=False)
    def clean(self):
        cleaned_data = super().clean()
        session_Debut = cleaned_data.get('session_Debut')
        session_Fin = cleaned_data.get('session_Fin')

        if session_Debut and session_Fin and session_Debut >= session_Fin:
            raise forms.ValidationError("La date de début de session doit être antérieure à la date de fin de session.")

        return cleaned_data

class EnseignerForm(forms.ModelForm):
    class Meta:
        model = Enseigner
        exclude = ['cours', 'professeur']
    titre = forms.CharField(max_length=30)
    libelle = forms.CharField(max_length=50)
    contenue_texte = forms.CharField(widget=forms.Textarea)
    urls = forms.CharField(widget=forms.Textarea)
    def clean(self):
        cleaned_data = super().clean()
        session_Debut = cleaned_data.get('session_Debut')
        session_Fin = cleaned_data.get('session_Fin')

        if session_Debut and session_Fin and session_Debut >= session_Fin:
            raise forms.ValidationError("La date de début de session doit être antérieure à la date de fin de session.")

        return cleaned_data

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        exclude=['cours']
        # fields = '__all__'  # Inclure tous les champs du modèle

# class ContenirForm(forms.ModelForm):
#     class Meta:
#         model = Contenir
#         fields = '__all__'  # Inclure tous les champs du modèle

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['full_name', 'message']


class ContactUsForm(forms.Form):
    name=forms.CharField(required=False)
    email=forms.EmailField()
    message=forms.CharField(max_length=500)
