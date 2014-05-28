# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Preguntes.forms import formulariPregunta, formulariTema, formulariPuntuacio
from django.contrib import messages
from django.http.response import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from Preguntes.models import tema, pregunta, tipus
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

@login_required
def afegirPuntuacio(request):
    if request.method == 'POST':
        form = formulariPuntuacio(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request,'Dades enviadades correctament')
            msg = "ok"
        else:
            msg = "fail"
        return HttpResponse(msg)
            
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
@login_required
def llistatPreguntes(request):
    preguntes = pregunta.objects.all()
    return render(request,'llistatPreguntes.html',{'preguntes':preguntes})
