from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.

class usuari(models.Model):
    user = models.OneToOneField(User)
    punts = models.IntegerField()
    
    
    def __unicode__(self):
        return self.usuari.username

medalles = (
    ('Nou','Nou'),
    ('CrearPreguntes','Crear noves preguntes'),
    ('EditarPreguntes','Editar preguntes erronies'),
    ('EliminarPreguntes','Eliminar preguntes'),
    )

class medalles(models.Model):
    nomMedalla =  models.CharField(max_length=100,choices = medalles,default='Nou')
    descripcio = models.CharField(max_length=200)
    puntsMinim = models.IntegerField()
    
class medallesUsuari(models.Model):
    medalla = ForeignKey(medalles)
    usuari = ForeignKey(User)
    
