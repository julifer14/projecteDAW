from django.conf.urls import patterns, url
from Preguntes import views 

urlpatterns = patterns('',
    url(r'^crearPregunta$', views.crearPregunta, name='crearPregunta'),
    url(r'^crearTema$', views.crearTema, name='crearTema'),
    url(r'^llistatTipus$',views.llistatTipus,name='llistatTipus'),
    url(r'^llistaTemes$',views.llistaTemes,name='llistaTemes$'),
    url(r'^preguntesTipus/(?P<tipusPregunta>\w+)$', views.practicarTipus, name='practicarTipus'),
    url(r'^llistatPreguntes$',views.llistatPreguntes,name='llistatPreguntes'),
    url(r'^afegirResposta', views.afegirResposta, name='afegirResposta'),
    url(r'^$',views.ferPreguntes,name='ferPreguntes'),
    url(r'^estadistiques$',views.estadistiques,name='estadistiques'),
    url(r'^preguntesIncorrectes',views.preguntesIncorrectes,name='preguntesIncorrectes'),
)