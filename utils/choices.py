from django.db import models



class Country(models.TextChoices):
    KAZ = ('K', 'Kaz')
    RUS = ('R', "Rus")
    TUR = ('T', "Tur")
    GER = ('G', "Ger")
    UKR = ('U', 'Ukr')
    DEN = ('D', "Den")
    BRA = ('B', "Bra")
    ITA = ('I', "Ita")
    NIG = ('N', "Nig")
    SPA = ('S', "Spa")
    AUS = ('A', "Aus")
    CAN = ('C', 'Can')
    POR = ('P', "Por")
    JAP = ('J', "Jap")
    VEN = ('V', "Ven")


class Role(models.TextChoices):
    GOA = ('G', "Goa")
    DEF = ('D', "Def")
    MID = ('M', "Mid")
    ATT = ('A', "Att")


