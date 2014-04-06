from django.contrib import admin
from Hashtags.models import Hashtag, Sugestao, SugestaoUsuario


class HashtagAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo', 'created_at', 'updated_at')

admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(Sugestao)
admin.site.register(SugestaoUsuario)
