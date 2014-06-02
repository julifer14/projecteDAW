# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Preguntes.forms import formulariPregunta, formulariTema, formulariResposta, formulariPreguntaErronea
from django.contrib import messages
from django.http.response import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from Preguntes.models import tema, pregunta, tipus,puntuacio,preguntaErronea
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from Usuaris.models import usuari, medallesUsuari
import json

@login_required
def exportXML(request):
    data = serializers.serialize("xml", pregunta.objects.all())
    return HttpResponse(data, content_type="application/xml")


#Mostra les preguntes marcades com erroneas
@login_required
def llistatPreguntesIncorrectes(request):
    medalles = medallesUsuari.objects.filter(usuari = request.user)
    pot = False
    for m in medalles:
        if m.medalla.nomMedalla == 'EliminarPreguntes':
            pot = True
    if pot:
        if request.method == 'POST':
            pass
        else:
            #mostrar llistat preguntes erronies amb mes de 5 entrades
            pass
        
#Nomes poden entrar els de la medalla ReportarPregunta
@login_required
def preguntesIncorrectes(request):
    medalles = medallesUsuari.objects.filter(usuari = request.user)
    pot = False
    for m in medalles:
        if m.medalla.nomMedalla == 'ReportarPregunta':
            pot = True
    
    if pot:
        if request.method == 'POST':
            preg = preguntaErronea()
            preg.usuariNotifica = request.user
            form = formulariPreguntaErronea(request.POST,instance = preg)
            if form.is_valid():
                form.save()
                messages.success(request,'Notificació enviada')
                #return HttpResponseRedirect(reverse('home'))
                msg = "ok"
            else:
                msg = "fail"
                messages.error(request, 'Hi ha hagut un error al notificar')
            return HttpResponse(msg)
    else:
        messages.error(request,'No tens permís per veure això!')
        return HttpResponseRedirect(reverse('home'))
        #form = formulariTema()
#Nomes poden entrar els de la medalla CrearPreguntes
@login_required
def crearPregunta(request):
    medalles = medallesUsuari.objects.filter(usuari = request.user)
    pot = False
    for m in medalles:
        print m.medalla.nomMedalla
        if m.medalla.nomMedalla == 'CrearPreguntes':
            pot = True
    
    print pot
    if pot:
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
    else:
        messages.error(request,'No tens permís per veure això!')
        return HttpResponseRedirect(reverse('home'))
#Per AJAX arriba un formulari amb el necessari per corregir
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
            #Sumar punts si ha aprovat!
            if nota >= 5:
                useret = usuari.objects.filter(user = request.user).get()
                useret.punts = useret.punts+2
                useret.save()
                messages.info(request,'Has guanyat dos punts al contestar la pregunta')
            #messages.success(request,'Dades enviadades correctament')
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
    
    
#Nomes poden entrar els de la medalla crear preguntes -- Si poden crear preguntes podran crear temes
@login_required
def crearTema(request):
    pot = False
    medalles = medallesUsuari.objects.filter(usuari = request.user)
    for m in medalles:
        if m.medalla.nomMedalla == 'CrearPreguntes':
            pot = True
    
    if pot:
        if request.method == 'POST':
            form = formulariTema(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Tema introduit correctament')
                #return HttpResponseRedirect(reverse('home'))
                msg = "ok"
                print form.cleaned_data['nom']
                t = tema.objects.filter(nom=form.cleaned_data['nom']).get()
                msg =  {"id": t.id, 
                            "nom": t.nom,
                            }
            else:
                msg = {"fail":"fail"}
                messages.error(request, 'Hi ha hagut un error al introduir el tema')
            return HttpResponse(json.dumps(msg), content_type="application/json")
    else:
        messages.error(request,'No tens permís per veure això!')
        return HttpResponseRedirect(reverse('home'))
#-------------------------------SENSE FER!
@login_required
def randomExamen(request):
    totesPreguntes = pregunta.objects.all()
    return render(request,'preguntesRandom.html')

#Vista que mostra l'exercici 
@login_required
def practicarTipus(request, tipusPregunta):
    tip = get_object_or_404(tipus,pk=tipusPregunta)
    medallesUser = medallesUsuari.objects.filter(usuari = request.user)
    try:
        preguntesTipus = pregunta.objects.filter(tipus = tipusPregunta)
    except:
        preguntesTipus = ""
    context = {'preguntesTipus':preguntesTipus,'tipus':tip,'medalles':medallesUser,}
    return render(request, 'preguntesTipus.html',context)

##########En desus ---- mostra els temes 
@login_required
def llistaTemes(request):
    if request.user.is_staff:
        temes = tema.objects.all()
        context = {'temes':temes}
        return render(request,'--llistatTemes.html',context)
    else:
        messages.error(request,'No tens permís per veure això!')
        return HttpResponseRedirect(reverse('home')) 

@login_required
def llistatTipus(request):
    tipusets = tipus.objects.all()
    context = {'tipus':tipusets}
    return render(request,'llistatTipus.html',context)

#Mostrar /preguntes
def ferPreguntes(request):
    #temes = tema.objects.all()
    return render(request,'preguntes.html')

@login_required
def estadistiques(request):
    #Estadistica de l'evolució de l'usuari
    punts = puntuacio.objects.filter(usuari = request.user)
    #Estadistica de la mitjana de les meves preguntes
    mevesPreguntes = pregunta.objects.filter(usuari = request.user)
    return render(request,'estadistiques.html', {'punts':punts,'mevesPreguntes':mevesPreguntes,})

######En desus ---- Mostra totes les preguntes
@login_required
def llistatPreguntes(request):
    preguntes = pregunta.objects.all()
    return render(request,'--llistatPreguntes.html',{'preguntes':preguntes})
