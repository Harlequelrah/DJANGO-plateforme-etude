from django.contrib import admin
from django.urls import path
from .forms import FeedbackForm
from .views import *
urlpatterns = [
    path('index/',index,name="index"),
    path('home/',home,name="home"),
    path('login/',login,name="login"),
    path('login/Utilisateur/',loginUtilisateur,name="loginUtilisateur"),
    path('login/Etudiant/',loginEtudiant,name="loginEtudiant"),
    path('login/professeur/',loginProfesseur,name="loginProfesseur"),
    path('signup/',signup,name="signup"),
    path('signupEtudiant/',signupEtudiant,name="signupEtudiant"),
    path('signupProfesseur/',signupProfesseur,name="signupProfesseur"),
    path('espaceEtudiant/<int:etudiant_id>',espaceEtudiant,name="espaceEtudiant"),
    path('espaceProfesseur/<int:professeur_id>',espaceProfesseur,name="espaceProfesseur"),

]
