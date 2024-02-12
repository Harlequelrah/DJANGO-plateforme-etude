from django.contrib import admin

# Register your models here.
from .models import *
class EtudiantAdmin(admin.ModelAdmin):
    list_display=('nom','prenom','email','password')

class ProfesseurAdmin(admin.ModelAdmin):
    list_display=('nom','prenom','email','password')

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('full_name','message')

admin.site.register(Etudiant,EtudiantAdmin)
admin.site.register(Professeur,ProfesseurAdmin)
admin.site.register(Feedback,FeedbackAdmin)
