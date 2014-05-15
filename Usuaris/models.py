from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuari(models.Model):
    usuari = models.OneToOneField(User)
    punts = models.IntegerField()
    
    
    def __unicode__(self):
        return self.usuari.username