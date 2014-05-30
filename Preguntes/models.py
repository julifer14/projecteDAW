# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import safe
from django.conf.urls import patterns
import re
# Create your models here.

class tema(models.Model):
    nom = models.CharField(max_length=100,unique= True)
    
    def __unicode__(self):
        return self.nom
    
class tipus(models.Model):
    nom = models.CharField(max_length=100,unique= True)
    
    def __unicode__(self):
        return self.nom

class pregunta(models.Model):
    tema = models.ForeignKey(tema)
    usuari = models.ForeignKey(User)
    tipus = models.ForeignKey(tipus)
    enunciat =  models.TextField(max_length=500)

    
    def __unicode__(self):
        return self.enunciat
    
    #Generar array de respostes
    def getRespostes(self):
        enunciat = self.enunciat
        respostes = re.findall(r"\[([A-Za-z]+)\]",enunciat)
        return respostes
        
    #Transformar l'enunciat a HTML
    def toHTML(self):
        text = self.enunciat
        canvi = ""
        if self.tipus.nom == "CompletarGramatica":
            canvi = "<input class='resposta' type='text'><br>"
        if self.tipus.nom == "EmplenarBuitsOrtografics":
            canvi = "<input class='form-control  inputPetit resposta' type='text'>"
        return safe(re.sub(r'\[\w+\]',canvi, text))
    
    
    
class puntuacio(models.Model):
    pregunta = models.ForeignKey(pregunta)
    usuari = models.ForeignKey(User)
    notaUsuari = models.IntegerField()
    data = models.DateField(auto_now_add=True,editable=False)
    hora = models.TimeField(auto_now_add=True,editable=False)
    correctes = models.IntegerField()
    incorrectes = models.IntegerField()
    
    def __unicode__(self):
        return self.nota 
    
class preguntaErronea(models.Model):
    pregunta = models.ForeignKey(pregunta)
    usuariNotifica = models.ForeignKey(User)
    data = models.DateField(auto_now_add=True,editable=False)
    hora = models.TimeField(auto_now_add=True,editable=False)
    
    
