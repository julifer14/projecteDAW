from django.conf.urls import patterns, url
from Usuaris import views 

urlpatterns = patterns('',
    url(r'^login$', views.entrada, name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^registre$',views.registrar,name='registre'),
)