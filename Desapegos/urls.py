from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url('^$', "Desapegos.views.index"),
	url('desapegar/', "Desapegos.views.desapegar"),
	url('usuario/(?P<uid>\w+)/$', "Desapegos.views.desapegos_de"),
	url('amigos/(?P<uid>\w+)/$', "Desapegos.views.desapegos_amigos"),
	url('salvar_amigos/', "Desapegos.views.guardar_amigos"),
	url('(?P<id>\d+)/$', "Desapegos.views.verDesapego"), 
)
