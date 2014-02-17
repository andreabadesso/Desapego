from django.conf.urls import patterns, url

urlpatterns = patterns('Hashtags.views',
	url(r'^hashtags/$', 'lista_hashtags')
)
