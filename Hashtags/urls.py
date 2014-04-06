from django.conf.urls import patterns, url

urlpatterns = patterns('Hashtags.views',
                       url(r'^sugerir/$', 'sugerir_hashtag'),
                       url(r'^sugestao_usuario/$', 'sugestao_usuario'),
                       url(r'^$', 'lista_hashtags')
                       )
