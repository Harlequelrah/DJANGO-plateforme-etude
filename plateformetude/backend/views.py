from django.shortcuts import render,redirect,get_object_or_404
from .forms import FeedbackForm
from .models import Feedback
from .models import *
from .forms import *
from .enums import Universite
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils import timezone



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




def addcourse(request,professeur_id,*args,**kwargs):
    professeur=get_object_or_404(Professeur, id=professeur_id)
    if request.method =='POST':
        form=EnseignerForm(request.POST)
        if form.is_valid():
            form.clean()
            titre=form.cleaned_data['titre']
            libelle=form.cleaned_data['libelle']
            contenue_texte=form.cleaned_data['contenue_texte']
            urls=form.cleaned_data['urls']
            cours= Cours.objects.create(titre=titre,libelle=libelle,contenue_texte=contenue_texte,urls=urls)
            session_Debut=form.cleaned_data['session_Debut']
            session_Fin=form.cleaned_data['session_Fin']
            volume_Horaire=form.cleaned_data['volume_Horaire']
            id_Session=form.cleaned_data['id_Session']
            enseigner=Enseigner.objects.create(id_Session=id_Session,professeur=professeur,cours=cours,session_Debut=session_Debut,session_Fin=session_Fin,volume_Horaire=volume_Horaire)
            messages.success(request,"Nouveau cours ajouté avec succès")
            return  redirect(listecours,professeur_id)
        else:
            messages.error(request,"Des erreurs ont été detecté veuillez reprendre")
    else:
        form=EnseignerForm()
    return  render(request,"addcourse.html",{})

def addmodule(request,professeur_id,*args,**kwargs):
    if request.method =='POST':
        form=ModuleForm(request.POST)
        print(form.errors)
        if form.is_valid():
            nom=form.cleaned_data["nom"]
            libelle=form.cleaned_data["libelle"]
            module= Module.objects.create(nom=nom,libelle=libelle)
            messages.success(request,"Nouveau Module ajouté avec succès")
            return  redirect(listecours,professeur_id)
        else:
            messages.error(request,"Des erreurs ont été detecté veuillez reprendre")
            return redirect(addmodule,professeur_id)
    else:
        form=ModuleForm()
    return  render(request,"addmodule.html",{'form':form})

def listecours(request,professeur_id,*args,**kwargs):
    professeur=get_object_or_404(Professeur,id=professeur_id)
    enseigners=Enseigner.objects.filter(professeur=professeur)
    modules=Module.objects.all()
    if request.method == 'POST':
        form=(request.POST)
        cours_instance=get_object_or_404(Cours,id=form.get('cours'))
        module_instance=get_object_or_404(Module,id=form.get('modules'))
        cours_instance.modules.add(module_instance)
        cours_instance.save()
        messages.success(request,"Votre cours a été ajouté au module")
        return redirect(listecours,professeur.id)
    courses=[enseigner.cours for enseigner in enseigners]
    # modules=Module.objects.filter(cours__in=courses)
    return render(request,"listecours.html",{'modules':modules,'enseigners':enseigners,'professeur':professeur,'courses':courses})
def updatecourse(request,professeur_id,cours_id,*args,**kwargs):
    professeur=get_object_or_404(Professeur,id=professeur_id)
    cours=get_object_or_404(Cours,id=cours_id)
    enseigner=get_object_or_404(Enseigner,professeur=professeur,cours=cours)
    if request.method=='POST':
        # print(request.POST)
        form=EnseignerUpdate(request.POST)
        # print(form.errors)
        if form.is_valid():
            if  'update' in request.POST:
                form.clean()
                titre=form.cleaned_data['titre']
                if titre:cours.titre=titre
                libelle=form.cleaned_data['libelle']
                if libelle:cours.libelle=form.cleaned_data['libelle']
                contenue_texte=form.cleaned_data['contenue_texte']
                if contenue_texte: cours.contenue_texte=form.cleaned_data['contenue_texte']
                urls=form.cleaned_data['urls']
                if urls: cours.urls=form.cleaned_data['urls']
                cours.save()
                session_debut = form.cleaned_data['session_Debut']
                if session_debut:
                    enseigner.session_Debut = session_debut

                session_fin = form.cleaned_data['session_Fin']
                if session_fin:
                    enseigner.session_Fin = session_fin

                volume_horaire = form.cleaned_data['volume_Horaire']
                if volume_horaire is not None:  # Vérification pour les champs de type IntegerField
                    enseigner.volume_Horaire = volume_horaire

                id_session = form.cleaned_data['id_Session']
                if id_session is not None:  # Vérification pour les champs de type IntegerField
                    enseigner.id_Session = id_session
                enseigner.save()
                messages.success(request,"Votre cours a été mis à jour avec succès")
                return  redirect(listecours,professeur_id)
            elif  'delete' in request.POST:
                course=cours.delete()
                course.save()
                # cours.save()
                # enseigner.delete()
                # enseigner.save()
                messages.success(request,"Votre cours a été supprimé")
                return  redirect(listecours,professeur_id)
        else:
            messages.error(request,"Des erreurs ont été detecté veuillez reprendre")
    else:
        form=EnseignerUpdate()
    return  render(request,"updatecourse.html",{"enseigner":enseigner})

def login(request,*args,**kwargs):
    return  render(request,"login.html",{})

# @login_required(login_url="templates/app/login/Etudiant/")
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


# @login_required(login_url="templates/app/login/Professeur/")
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



def espaceEtudiant(request,etudiant_id,*args,**kwargs):
    etudiant = get_object_or_404(Etudiant, id=etudiant_id)
    return render(request,"espaceEtudiant.html",{'etudiant':etudiant})
def espaceProfesseur(request,professeur_id,*args,**kwargs):
    professeur = get_object_or_404(Professeur, id=professeur_id)
    return render(request,"espaceProfesseur.html",{'professeur':professeur})

def signup(request,*args,**kwargs):

    return  render(request,"signup.html",{})

def cours(request,etudiant_id,*args,**kwargs):
    modules=Module.objects.all()
    return render(request,"cours.html",{'modules':modules,'etudiant_id':etudiant_id})

def coursdetail(request,etudiant_id,cours_id,*args,**kwargs):
    cours=get_object_or_404(Cours,id=cours_id)
    enseigners = Enseigner.objects.filter(cours=cours, session_Debut__lte=timezone.now(), session_Fin__gte=timezone.now()).all()
    etudiant=get_object_or_404(Etudiant,id=etudiant_id)
    if request.method=='POST':
        form=(request.POST)
        id_Session=form.get('id_Session')
        id_Session=int(id_Session)
        inscription=Inscription.objects.create(id_Session=id_Session,etudiant=etudiant,cours=cours)
        messages.success(request,"Votre inscription s est déroulée a merveille")
        return redirect("espaceEtudiant",etudiant_id)
    return render(request,"coursdetail.html",{'etudiant_id':etudiant_id,'cours':cours,'enseigners':enseigners})

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



def creationCours(request,*args,**kwargs):
    return render(request,"creationCours.html",{})

def inscriptionCours(request,*args,**kwargs):
    return render(request,"inscriptionCours.html",{})
# Create your views here.

def contact(request,*args,**kwargs):
    if request.method=='POST':
        form=ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data["email"]or "anonymous"} Via LearnEd Contact Us Form",
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=['learned@.com'],
            )
            messages.success(request,"Nous avons bien reçu votre email")
            return redirect(home)

    else:form=ContactUsForm()

    return render(request,"contact.html",{'form':form})
