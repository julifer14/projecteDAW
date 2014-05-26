from django.conf.urls import patterns, url
from Preguntes import views 

urlpatterns = patterns('',
    url(r'^crearPregunta$', views.crearPregunta, name='crearPregunta'),
    url(r'^crearTema$', views.crearTema, name='crearTema'),
    url(r'^llistatTipus$',views.llistatTipus,name='llistatTipus'),
    url(r'^preguntesTipus/(?P<tipusPregunta>\w+)$', views.practicarTipus, name='practicarTipus'),
    url(r'^llistatPreguntes$',views.llistatPreguntes,name='llistatPreguntes'),
    url(r'^afegirPuntuacio$', views.afegirPuntuacio, name='afegirPuntuacio'),
    url(r'^$',views.ferPreguntes,name='ferPreguntes'),
)