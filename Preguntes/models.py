# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tema(models.Model):
    nom = models.CharField(max_length=100,unique= True)
    
    def __unicode__(self):
        return self.nom

tipus = (
    ('EmplenarBuitsOrtografics','Emplenar Buits d\'ortografia'),
    ('CompletarGramatica','Completar gramatica'),
    ('Test','Test'),
    ('Relacionar','Relacionar'),
    )
    
class pregunta(models.Model):
    tema = models.ForeignKey(tema)
    usuari = models.ForeignKey(User)
    tipus = models.CharField(max_length=100,choice=tipus)
    enunciat =  models.CharField(max_length=500)

    
    def __unicode__(self):
        return self.enunciat
    
    
    
class puntuacio(models.Model):
    pregunta = models.ForeignKey(pregunta)
    usuari = models.ForeignKey(User)
    notaUsuari = models.IntegerField()
    data = models.DateField()
    hora = models.TimeField()
    
    def __unicode__(self):
        return "Usuari " + self.usuari + " pregunta: " + self.pregunta.id + " punts " + self.notaUsuari 
    
class preguntaErronea(models.Model):
    pregunta = models.ForeignKey(pregunta)
    usuariNotifica = models.ForeignKey(User)
    data = models.DateField()
    hora = models.TimeField()
    
    
