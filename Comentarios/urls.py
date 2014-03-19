from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	# http://<url>/comentarios/comentar/<id do desapego>/<facebook id>/?comentario=<comentario>
	url('comentar/(?P<id>\d+)/(?P<fbid>\w+)/$', "Comentarios.views.comentar"),
	# http://<url>/<desapego id>/
	url('desapego/(?P<id>\d+)/$', "Comentarios.views.comentarios_desapego"),
	# http://<url>/comentarios/
	url('^$', "Comentarios.views.todos_comentarios"),
)
