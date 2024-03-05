from django.contrib import admin
from django.urls import path
from .forms import FeedbackForm
from .views import *
urlpatterns = [
    path('index/',index,name="index"),
    path('home/',home,name="home"),
    path('cours/addcourse/<int:professeur_id>/',addcourse,name="addcourse"),
    path('cours/updatecourse/<int:professeur_id>/<int:cours_id>/',updatecourse,name="updatecourse"),
    path('cours/listecours/<int:professeur_id>/',listecours,name="listecours"),
    path('cours/addmodule/<int:professeur_id>/',addmodule,name="addmodule"),
    path('contact/',contact,name="contact"),
    path('login/',login,name="login"),
    path('login/Utilisateur/',loginUtilisateur,name="loginUtilisateur"),
    path('login/Etudiant/',loginEtudiant,name="loginEtudiant"),
    path('login/professeur/',loginProfesseur,name="loginProfesseur"),
    path('signup/',signup,name="signup"),
    path('signupEtudiant/',signupEtudiant,name="signupEtudiant"),
    path('signupProfesseur/',signupProfesseur,name="signupProfesseur"),
    path('espaceEtudiant/<int:etudiant_id>',espaceEtudiant,name="espaceEtudiant"),
    path('espaceProfesseur/<int:professeur_id>/',espaceProfesseur,name="espaceProfesseur"),
    path('creation/Cours/',creationCours,name="creationCours"),
    path('cours/<int:etudiant_id>/',cours,name="cours"),
    path('cours/<int:etudiant_id>/<int:cours_id>/',coursdetail,name="coursdetail"),

]
