from django import  forms
from Usuaris.models import usuari

class formulariLogin(forms.Form):
    usuari = forms.CharField(max_length=100)
    contrasenya = forms.CharField(max_length=100, widget=forms.PasswordInput() )
    
class formulariRegistre(forms.Form):
    nom = forms.CharField(max_length=100,label = 'Nom')
    cognom = forms.CharField(max_length=100,label = 'Cognom')
    usuari = forms.CharField(max_length=100, label = 'Nom d\'usuari')
    correu = forms.CharField(max_length=100,label = 'Correu electronic')
    contrasenya = forms.CharField(max_length=100, widget=forms.PasswordInput(), label = 'Contrasenya' )
    confirmacioContrasenya = forms.CharField(max_length=100, widget=forms.PasswordInput(), label = 'Confirmeu la contrasenya' )
    
