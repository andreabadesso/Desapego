from django.forms import widgets
from rest_framework import serializers
from Comentarios.models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
	class Meta:
		model=Comentario
		depth=1
		fields = ("id", "usuario", "comentario", "created_at", "updated_at")
