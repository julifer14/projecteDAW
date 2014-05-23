from django import  forms
from Preguntes.models import pregunta, tema,puntuacio

class formulariPregunta(forms.ModelForm):
    class Meta:
        model = pregunta
        fields = ['tema','tipus','enunciat']
        
class formulariTema(forms.ModelForm):
    class Meta:
        model = tema
        fields = ['nom']
        
class formulariPuntuacio(forms.ModelForm):
    class Meta:
        model = puntuacio
        exclude = ['data','hora']