# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Preguntes.forms import formulariPregunta, formulariTema
from django.contrib import messages
from django.http.response import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from Preguntes.models import tema, pregunta
from django.contrib.auth.models import User

# Create your views here.
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
            #return HttpResponseRedirect(reverse('home'))
    else:
        form = formulariPregunta(instance = preg)
        
    camps_bootestrapejar =( 'tema', 'tipus','enunciat')
    for c in camps_bootestrapejar:
        form.fields[c].widget.attrs['class'] = 'form-control'
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

@login_required
def randomExamen(request):
    totesPreguntes = pregunta.objects.all()
    return render(request,'preguntesRandom.html')

@login_required
def practicarTema(request, idTema):
    temeta = get_object_or_404(tema, pk = idTema)
    preguntesTema = pregunta.objects.filter(tema = idTema)
    context = {'preguntesTema':preguntesTema,'tema':temeta}
    return render(request, 'preguntesTema.html',context)

def llistaTemes(request):
    temes = tema.objects.all()
    context = {'temes':temes}
    return render(request,'llistatTemes.html',context)

def ferPreguntes(request):
    #temes = tema.objects.all()
    return render(request,'preguntes.html')
