from django.conf.urls import patterns, url
from Preguntes import views 

urlpatterns = patterns('',
    url(r'^crearPregunta$', views.crearPregunta, name='crearPregunta'),
    url(r'^crearTema$', views.crearTema, name='crearTema'),
    url(r'^llistatTemes$',views.llistaTemes,name='llistatTemes'),
    url(r'^preguntesTema/(?P<idTema>\d+)$', views.practicarTema, name='practicarTema'),
    url(r'^llistatPreguntes$',views.llistatPreguntes,name='llistatPreguntes'),
    #url(r'^respostes$', views.respostes, name='respostes'),
    url(r'^$',views.ferPreguntes,name='ferPreguntes'),
)