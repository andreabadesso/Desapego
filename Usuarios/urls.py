from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'(?P<fbid>\w+)/$', "Usuarios.views.verUsuario"),
)
