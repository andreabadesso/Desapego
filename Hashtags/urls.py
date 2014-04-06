from django.conf.urls import patterns, url

urlpatterns = patterns('Hashtags.views',
                       url(r'^sugerir/$', 'sugerir_hashtag'),
                       url(r'^$', 'lista_hashtags')
                       )
