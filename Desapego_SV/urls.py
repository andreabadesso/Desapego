from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Admin
                       url(r'^$', "Site.views.index"),
                       url(r'^admin/', include(admin.site.urls)),
                       # Usuarios
                       url(r'^usuarios/', include('Usuarios.urls')),
                       # Desapegos
                       url(r'^desapegos/', include("Desapegos.urls")),
                       # Comentarios
                       url(r'^comentarios/', include("Comentarios.urls")),
                       # Hashtags
                       url(r'^hashtags/', include('Hashtags.urls')),
                       # Status
                       url(r'^status/', include('Status.urls')),
                       # Curtir
                       url(r'^curtirDesapego/$',
                           "Desapegos.views.curtirDesapego"),
                       url(r'^verificarCurtida/$',
                           "Desapegos.views.verificarCurtida"),
                       # Ver usuario (WEB)
                       url(r'(?P<id>\d+)/$', "Site.views.desapego"),
                       url(r'^politica_de_privacidade',
                           "Desapegos.views.policy"),
                       )
