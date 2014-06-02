from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.contrib import messages
# Create your models here.

class usuari(models.Model):
    user = models.OneToOneField(User)
    punts = models.IntegerField()
    
    
    def __unicode__(self):
        return self.user.username
    


def comprovar_medalles(sender, instance, created, **kwargs):
    puntsUsuari = instance.punts
    usu =  instance.user
    llistaMedallesUsuari = medalles.objects.filter(medallesusuari__usuari=usu)
    medallesPosibles = medalles.objects.filter(puntsMinim__lte=puntsUsuari)
    #Si no es troba a la llista li assigno
    #noves_medalles = []
    for m in medallesPosibles:
        if m not in llistaMedallesUsuari:
            medallaUsu = medallesUsuari()
            medallaUsu.usuari = usu
            medallaUsu.medalla = m 
            medallaUsu.save()
            #noves_medalles.add( 'Has aconseguit la medalla %s' % m )
    #instance.noves_medalles = noves_medalles
    
        

post_save.connect(comprovar_medalles, sender = usuari)

medalles = (
    ('Nou','Nou'),
    ('CrearPreguntes','Crear noves preguntes'),
    ('EditarPreguntes','Editar preguntes erronies'),
    ('EliminarPreguntes','Eliminar preguntes'),
    ('ReportarPregunta','Reportar Pregunta'),
    )

class medalles(models.Model):
    nomMedalla =  models.CharField(max_length=100,choices = medalles,default='Nou')
    descripcio = models.CharField(max_length=200)
    puntsMinim = models.IntegerField()
    
    def __unicode__(self):
        return self.nomMedalla
    
class medallesUsuari(models.Model):
    medalla = ForeignKey(medalles)
    usuari = ForeignKey(User)
    
