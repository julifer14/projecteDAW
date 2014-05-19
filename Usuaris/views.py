# -*- encoding: utf-8 -*-
from django.shortcuts import render
from Usuaris.forms import formulariLogin, formulariRegistre
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from Usuaris.models import usuari

# Create your views here.

def registrar(request):
    if request.method == 'POST':
        form = formulariRegistre(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            cognom = form.cleaned_data['cognom']
            usuariT = form.cleaned_data['usuari']
            correu = form.cleaned_data['correu']
            contrasenya = form.cleaned_data['contrasenya']
            confirmacioContrasenya = form.cleaned_data['confirmacioContrasenya']
            comprovacioUsuari = User.objects.filter(username = usuariT).count()
            if comprovacioUsuari==0:
                if contrasenya == confirmacioContrasenya:
                    user = User.objects.create_user(usuariT,correu,contrasenya)
                    user.first_name = nom
                    user.last_name = cognom
                    user.save()
                    perfil = usuari()
                    perfil.user = user
                    perfil.punts = 10
                    perfil.save()
                    userAuth = authenticate(username = usuariT,password = contrasenya)
                    if userAuth is not None:
                        #Pot ser que l'usuari estigui descativat! s'ha de comprovar
                        if userAuth.is_active:
                            #Fem login
                            login(request, userAuth)
                            messages.success(request, 'Login correcte')
                            next = request.GET.get('next','/')
                            return HttpResponseRedirect(next)
                            # Redirect to a success page.
                        else:
                            messages.error(request, 'Compte desactivada, contacti amb l\'administrador')
                    # Return a 'disabled account' error message
                    else:
                        messages.error(request, 'Ep! Hi ha hagut un error!')
                # Return an 'invalid login' error message.
                else:
                    messages.error(request,'Les contrasenyes no coincideixen')
            else:
                messages.error(request,'L\'usuari ja es troba al sistema')
        else:
            messages.error(request, 'Ep! Hi ha hagut un error!')
            #Si no es pots es GET i vol dir que no tenim dades a processar
    else:
        form = formulariRegistre() 
        
    #Afegir la clase de bootstrap als camps
    camps_bootestrapejar =( 'usuari', 'contrasenya','cognom','nom','correu','confirmacioContrasenya')
    for c in camps_bootestrapejar:
        form.fields[c].widget.attrs['class'] = 'form-control'
    form.fields['usuari'].widget.attrs['placeholder'] = 'Usuari'
    form.fields['contrasenya'].widget.attrs['placeholder'] = 'Contrasenya'
    form.fields['cognom'].widget.attrs['placeholder'] = 'Cognom'
    form.fields['nom'].widget.attrs['placeholder'] = 'Nom'
    form.fields['correu'].widget.attrs['placeholder'] = 'Correu electrònic'
    form.fields['confirmacioContrasenya'].widget.attrs['placeholder'] = 'Confirmar la contrasenya'
    
    return render(request, 'registre.html', {'form': form,})


   

def entrada(request):
    #Si el metode es POST m'ho en enviat a mi mateix vol dir que ja tinc dades per processar
    if request.method == 'POST': 
        form = formulariLogin(request.POST)
        #Si les dades entrades són correctes (compleixen el tipus de camp...) Procesem i redirigim a portada
        if form.is_valid():
            #Emmagatzemem les dades que es troben al diccioanri form.cleaned_data a les variables corresponents
            username = form.cleaned_data['usuari']
            password = form.cleaned_data['contrasenya']
            #Autenticar usuaris
            user = authenticate(username=username, password=password)
            #Si es tot correcte
            if user is not None:
                #Pot ser que l'usuari estigui descativat! s'ha de comprovar
                if user.is_active:
                    #Fem login
                    login(request, user)
                    messages.success(request, 'Login correcte')
                    next = request.GET.get('next','/')
                    return HttpResponseRedirect(next)
                    # Redirect to a success page.
                else:
                    messages.error(request, 'Compte desactivada, contacti amb l\'administrador')
            # Return a 'disabled account' error message
            else:
                messages.error(request, 'Ep! Hi ha hagut un error!')
        # Return an 'invalid login' error message.
            
        else:
            messages.error(request, 'Ep! Hi ha hagut un error!')
        #Si no es pots es GET i vol dir que no tenim dades a processar
    else:
        form = formulariLogin() 
        

    #Afegir la clase de bootstrap als camps
    camps_bootestrapejar =( 'usuari', 'contrasenya')
    for c in camps_bootestrapejar:
        form.fields[c].widget.attrs['class'] = 'form-control'
    form.fields['usuari'].widget.attrs['placeholder'] = 'Usuari'
    form.fields['contrasenya'].widget.attrs['placeholder'] = 'Contrasenya'
    return render(request, 'login.html', {
        'form': form,
    })
    
#La funció logout fa sortir a l'usuari
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout correcte, a reveure')
    return HttpResponseRedirect('/')