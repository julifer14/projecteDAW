# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Preguntes.forms import formulariPregunta, formulariTema, formulariResposta
from django.contrib import messages
from django.http.response import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from Preguntes.models import tema, pregunta, tipus,puntuacio
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
import json

@login_required
def crearPregunta(request):
    preg = pregunta()
    preg.usuari = request.user
    if request.method == 'POST':
        form = formulariPregunta(request.POST,instance = preg)
        if form.is_valid():
            form.save()
            messages.success(request,'Pregunta introduida correctament')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Hi ha hagut un error al introduir la pregunta')
    else:
        form = formulariPregunta(instance = preg)
        
    camps_bootestrapejar =( 'tema', 'tipus','enunciat')
    for c in camps_bootestrapejar:
        form.fields[c].widget.attrs['class'] = 'form-control'
    return render(request, 'crearPregunta.html', {'form':form,})
#Per AJAX arriba un formulari amb la pregunta que ha contestat l'usuari i les respostes que 
@login_required
def afegirResposta(request):
    if request.method == 'POST':
        form = formulariResposta(request.POST)
        if form.is_valid():
            idPregunta = form.cleaned_data['idPregunta']
            respostes = form.cleaned_data['respostes']
            pregun = get_object_or_404(pregunta,pk=idPregunta)
            nota = 0
            correcte = 0
            incorrecte = 0
            arrayRespostesUsuari = respostes.split(',')
            #El model té una funció que retorna les respostes en un array
            arrayRespostesCorrectes = pregun.getRespostes()
            #Comprovació de les respostes
            if arrayRespostesCorrectes == arrayRespostesUsuari:
                nota = 10
                correcte = len(arrayRespostesCorrectes)
            else:
                
                for i in xrange(len(arrayRespostesCorrectes)):
                    if arrayRespostesCorrectes[i] == arrayRespostesUsuari[i]:
                        correcte= correcte+1
                    else:
                        incorrecte = incorrecte+1
                notaPerPregunta = 10/(correcte+incorrecte)
                nota = correcte*notaPerPregunta
            puntu = puntuacio()
            puntu.pregunta = pregun
            puntu.usuari = request.user
            puntu.notaUsuari = nota
            puntu.correctes = correcte
            puntu.incorrectes = incorrecte
            puntu.save()
            messages.success(request,'Dades enviadades correctament')
            #preparem la llista de noms a enviar
            resposteta =  {"idPregunta": idPregunta, 
                            "nota": nota,
                            "correctes":correcte,
                            "incorrectes":incorrecte
                            }
        return HttpResponse(json.dumps(resposteta), content_type="application/json")
            
    else:
        messages.error(request,'No tens permís per veure això!')
        return HttpResponseRedirect(reverse('home'))
    
    

@login_required
def crearTema(request):
    if request.method == 'POST':
        form = formulariTema(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tema introduit correctament')
            #return HttpResponseRedirect(reverse('home'))
            msg = "ok"
        else:
            msg = "fail"
            messages.error(request, 'Hi ha hagut un error al introduir el tema')
        return HttpResponse(msg)
    else:
        messages.error(request,'No tens permís per veure això!')
        return HttpResponseRedirect(reverse('home'))
        #form = formulariTema()
        
    #camps_bootestrapejar =( 'nom',)
    #for c in camps_bootestrapejar:
    #    form.fields[c].widget.attrs['class'] = 'form-control'
    #form.fields['nom'].widget.attrs['placeholder'] = 'Nom del tema'
    #return render(request,'crearTema.html',{'form':form,})


@login_required
def randomExamen(request):
    totesPreguntes = pregunta.objects.all()
    return render(request,'preguntesRandom.html')

##Vista que mostra l'exercici 
@login_required
def practicarTipus(request, tipusPregunta):
    tip = get_object_or_404(tipus,pk=tipusPregunta)
    try:
        preguntesTipus = pregunta.objects.filter(tipus = tipusPregunta)
    except:
        preguntesTipus = ""
    context = {'preguntesTipus':preguntesTipus,'tipus':tip}
    return render(request, 'preguntesTipus.html',context)

def llistaTemes(request):
    temes = tema.objects.all()
    context = {'temes':temes}
    return render(request,'llistatTemes.html',context)

@login_required
def llistatTipus(request):
    tipusets = tipus.objects.all()
    context = {'tipus':tipusets}
    return render(request,'llistatTipus.html',context)

def ferPreguntes(request):
    #temes = tema.objects.all()
    return render(request,'preguntes.html')

def estadistiques(request):
    return render(request,'estadistiques.html')

@login_required
def llistatPreguntes(request):
    preguntes = pregunta.objects.all()
    return render(request,'llistatPreguntes.html',{'preguntes':preguntes})
