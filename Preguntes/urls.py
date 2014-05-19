from django.conf.urls import patterns, url
from Preguntes import views 

urlpatterns = patterns('',
    url(r'^crearPregunta$', views.crearPregunta, name='creaPregunta'),
    url(r'^crearTema$', views.crearTema, name='creaTema'),
    #url(r'^logout$', views.logout_view, name='logout'),
)