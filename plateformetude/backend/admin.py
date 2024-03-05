from django.contrib import admin

# Register your models here.
from .models import *
class EtudiantAdmin(admin.ModelAdmin):
    list_display=('nom','prenom','email','password')

class ProfesseurAdmin(admin.ModelAdmin):
    list_display=('nom','prenom','email','password')

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('full_name','message')

class ModuleAdmin(admin.ModelAdmin):
    list_display=('nom','libelle')

class CoursAdmin(admin.ModelAdmin):
    list_display=('titre','libelle')

class EnseignerAdmin(admin.ModelAdmin):
    list_display=('id_Session','session_Debut','session_Fin','volume_Horaire')
class InscriptionAdmin(admin.ModelAdmin):
    list_display=('id_Session','status','etudiant','cours','date_Inscription')

admin.site.register(Etudiant,EtudiantAdmin)
admin.site.register(Professeur,ProfesseurAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Cours,CoursAdmin)
admin.site.register(Module,ModuleAdmin)
admin.site.register(Enseigner,EnseignerAdmin)
admin.site.register(Inscription,InscriptionAdmin)
