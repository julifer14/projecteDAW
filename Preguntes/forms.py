from django import  forms
from Preguntes.models import pregunta, tema

class formulariPregunta(forms.ModelForm):
    class Meta:
        model = pregunta
        fields = ['tema','tipus','enunciat']
        
class formulariTema(forms.ModelForm):
    class Meta:
        model = tema
        fields = ['nom']