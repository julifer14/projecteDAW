from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PreguntMatic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'eines.views.home', name='home'),
    url(r'^preguntes/', include('Preguntes.urls', namespace='preguntes')),
    url(r'^usuaris/', include('Usuaris.urls', namespace='usuaris')),
    url(r'^admin/', include(admin.site.urls)),
)
