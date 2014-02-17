from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^desapegos/', "Desapegos.views.index"),
    url(r'^usuario/$', "Usuarios.views.verUsuario"),
    url(r'^desapego/$', "Desapegos.views.verDesapego"),
    url(r'^desapegar', "Desapegos.views.desapegar"),
    url(r'^meus_desapegos/$', "Desapegos.views.meusDesapegos"),
    url(r'^desapegos_amigos/$', "Desapegos.views.desapegos_amigos"),
    url(r'^', include('Hashtags.urls')),

)
