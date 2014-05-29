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
        
class formulariResposta(forms.Form):
    idPregunta = forms.IntegerField()
    respostes = forms.CharField(max_length=300)