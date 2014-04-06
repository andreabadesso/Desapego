from django.contrib import admin
from Hashtags.models import Hashtag, Sugestao


class HashtagAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo', 'created_at', 'updated_at')

admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(Sugestao)
