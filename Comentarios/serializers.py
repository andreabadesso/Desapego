from django.forms import widgets
from rest_framework import serializers
from Comentarios.models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
	usuario = serializers.SlugRelatedField(many=False, read_only=True,
						  slug_field='nome_completo')
	
	class Meta:
		model=Comentario
		fields = ("id", "usuario", "comentario", "created_at", "updated_at")
