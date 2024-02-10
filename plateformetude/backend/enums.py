from enum import Enum
from django.db import models
class InscriptionStatuts(models.TextChoices):
    EN_COURS = "E_C"
    EN_ATTENTE = "E_A"
    VALIDE = "VL"
    ANNULEE = "AN"

class Universite(models.TextChoices):
    IAI_TOGO="IAI"
    UNIVERSITE_DE_LOME="UL"
    UCAO_UUT="UC"
    ISDI="IS"
    FORMATEC="FMT"
    LOME_BUISNESS_SCHOOL="LBS"
    ISMAD="ISM"
    DEFITECH="DFT"
    ISFODEME="ISF"
    ISTM="IM"
    ISLA="IA"
    ESTABAT="ETB"
    CIFOP="CFP"
    ECOLE_DES_CADRES="EC"

