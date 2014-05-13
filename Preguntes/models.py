# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class tipusPregunta(models.Model):
    nom = models.CharField(max_length=100,unique= True)
    enunciatModel = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.noms