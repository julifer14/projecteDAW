# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tipusPregunta(models.Model):
    nom = models.CharField(max_length=100,unique= True)
    enunciatModel = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.noms
    
class pregunta(models.Model):
    enunciat =  models.CharField(max_length=500)
    tipus = models.ForeignKey(tipusPregunta)
    usuari = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.enunciat
    
class respostaUsuari(models.Model):
    pregunta =  models.ForeignKey(pregunta)
    usuari = models.ForeignKey(User)
    respostaUsuari = models.CharField(max_length=500)
    
    def __unicode__(self):
        return self.respostaUsuari
    
class preguntaErronea(models.Model):
    pregunta = models.ForeignKey(pregunta)
    usuariNotifica = models.ForeignKey(User)
    data = models.DateField()
    hora = models.TimeField()
    