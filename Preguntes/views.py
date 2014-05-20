# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Preguntes.forms import formulariPregunta, formulariTema
from django.contrib import messages
from django.http.response import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from Preguntes.models import tema
from django.contrib.auth.models import User

# Create your views here.
@login_required
def crearPregunta(request):
    if request.method == 'POST':
        form = formulariPregunta(request.POST)
        form.usuari = request.user
        if form.is_valid():
            print form.usuari
            form.save()
            messages.success(request,'Pregunta introduida correctament')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Hi ha hagut un error al introduir la pregunta')
            return HttpResponseRedirect(reverse('home'))
    else:
        form = formulariPregunta()
        
    camps_bootestrapejar =( 'tema', 'tipus','enunciat')
    for c in camps_bootestrapejar:
        form.fields[c].widget.attrs['class'] = 'form-control'
    form.fields['usuari'].widget.attrs['hidden'] =''
    return render(request, 'crearPregunta.html', {'form':form,})

@login_required
def crearTema(request):
    if request.method == 'POST':
        form = formulariTema(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Tema introduit correctament')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Hi ha hagut un error al introduir el tema')
    else:
        form = formulariTema()
        
    camps_bootestrapejar =( 'nom',)
    for c in camps_bootestrapejar:
        form.fields[c].widget.attrs['class'] = 'form-control'
    form.fields['nom'].widget.attrs['placeholder'] = 'Nom del tema'
    return render(request,'crearTema.html',{'form':form,})

def llistaTemes(request):
    temes = tema.objects.all()
    context = {'temes':temes}
    #crear html!
    return render(request,'llistatTemes.html',context)

def ferPreguntes(request):
    temes = tema.objects.all()
    return render(request,'preguntes.html',{'temes':temes})
