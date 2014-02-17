from django.contrib import admin
from Hashtags.models import Hashtag

class HashtagAdmin(admin.ModelAdmin):
        list_display = ('nome', 'sexo', 'created_at', 'updated_at') 

admin.site.register(Hashtag, HashtagAdmin)
