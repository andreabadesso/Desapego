from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'usuario/(?P<fbid>\w+)/$', "Usuarios.views.verUsuario"),
)
