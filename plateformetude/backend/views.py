from django.shortcuts import render,redirect
from .forms import FeedbackForm
from .models import Feedback
from .models import *
from .forms import *
from .enums import Universite
from django.contrib import messages

# Create your views here.
def index(request,*args,**kwargs):
    return  render(request,"index.html",{})

def home(request,*args,**kwargs):
    feedback=Feedback.objects.all()[:10]
    if request.method == 'POST' and 'feedbacksub' in request.POST:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Merci de nous avoir partagé votre avis")
    else:
        form = FeedbackForm()
    return  render(request,"home.html", {'form': form,'feedback':feedback})


def login(request,*args,**kwargs):
    return  render(request,"login.html",{})

def loginEtudiant(request,*args,**kwargs):
    if request.method=='POST':
        #print("la requete est post")
        form=UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            #print("formulaire validé")
            try:
                etudiant=Etudiant.objects.get(email=email)
            except Etudiant.DoesNotExist:
                #print("L ' email saisi n ' est lié à aucun compte")
                messages.error(request,"L ' email saisi n ' est lié à aucun compte")
                return render(request,"loginUtilisateur.html",{'form':form})
            else:
                if etudiant:
                    #print("y a un utilisateur")
                    if etudiant.verify_password(password):
                        #print("mot de passe correcte")
                        messages.success(request,f"Nous sommes ravi de vous revoir ,{etudiant.nom} {etudiant.prenom}")
                        return redirect("espaceEtudiant",etudiant.id)
                    else:
                        #print("mot de passe incorrecte")
                        messages.error(request,"Le mot de passe saisi est incorrect , veuillez reprendre")
                        return render(request,"loginUtilisateur.html",{'form':form})
        #print("formulaire invalide")
        return render(request,"loginUtilisateur.html",{'form':form})
    else:
        #print("c est un get")
        return render(request,"loginUtilisateur.html",{})

def loginUtilisateur(request,*args,**kwargs):
    return render(request,"loginUtilisateur.html")



def loginProfesseur(request,*args,**kwargs):
    if request.method=='POST':
        #print("la requete est post")
        form=UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            #print("formulaire validé")
            try:
                professeur=Professeur.objects.get(email=email)
            except Professeur.DoesNotExist:
                #print("L ' email saisi n ' est lié à aucun compte")
                messages.error(request,"L ' email saisi n ' est lié à aucun compte")
                return render(request,"loginUtilisateur.html",{'form':form})
            else:
                if professeur:
                    #print("y a un utilisateur")
                    if professeur.verify_password(password):
                        #print("mot de passe correcte")
                        messages.success(request,f"Nous sommes ravi de vous revoir ,{professeur.nom} {professeur.prenom}")
                        return redirect("espaceProfesseur",professeur.id)
                    else:
                        #print("mot de passe incorrecte")
                        messages.error(request,"Le mot de passe saisi est incorrect , veuillez reprendre")
                        return render(request,"loginUtilisateur.html",{'form':form})
        #print("formulaire invalide")
        return render(request,"loginUtilisateur.html",{'form':form})
    else:
        #print("c est un get")
        return render(request,"loginUtilisateur.html",{})



def espaceEtudiant(request,*args,**kwargs):
    return render(request,"espaceEtudiant.html")
def espaceProfesseur(request,*args,**kwargs):
    return render(request,"espaceProfesseur.html")

def signup(request,*args,**kwargs):

    return  render(request,"signup.html",{})

def signupEtudiant(request,*args,**kwargs):
    universites = Universite.choices
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            etudiant=form.save(commit=False)
            etudiant.set_password(password)
            etudiant.save()
            messages.success(request,f"Felicitation ,{etudiant.nom} {etudiant.prenom} votre inscription est un succès")
            return redirect("home")
        return  render(request,"signupEtudiant.html",{'universites':universites,'etudiant':etudiant})
    else:return  render(request,"signupEtudiant.html",{'universites':universites,'etudiant':{}})

def signupProfesseur(request,*args,**kwargs):
    if request.method == 'POST':
        form = ProfesseurForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            professeur=form.save(commit=False)
            professeur.set_password(password)
            professeur.save()
            messages.success(request,f"Felicitation,{professeur.nom} {professeur.prenom} votre inscription est un succès")
            return  redirect("home")
        return  render(request,"signupProfesseur.html",{'professeur':professeur})
    else: return  render(request,"signupProfesseur.html",{'professeur':{}})




# Create your views here.
