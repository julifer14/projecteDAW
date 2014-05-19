from django.conf.urls import patterns, url
from Preguntes import views 

urlpatterns = patterns('',
    url(r'^crearPregunta$', views.crearPregunta, name='crearPregunta'),
    url(r'^crearTema$', views.crearTema, name='crearTema'),
    url(r'^llistatTemes$',views.llistaTemes,name='llistatTemes'),
    url(r'^',views.ferPreguntes,name='ferPreguntes'),
    
    #url(r'^logout$', views.logout_view, name='logout'),
)