from django.forms import widgets
from rest_framework import serializers
from Desapegos.models import Desapego

class DesapegoSerializer(serializers.ModelSerializer):
	usuario = serializers.SlugRelatedField(many=False, read_only=True,
						  slug_field='nome_completo')

	alvo = serializers.SlugRelatedField(many=False, read_only=True,
						  slug_field='nome_completo')

	hashtags = serializers.SlugRelatedField(many=True, read_only=True,
						  slug_field='nome')
	alvoid = serializers.Field()
	usuarioid = serializers.Field()

	class Meta:
		model=Desapego
		fields = ("id", "alvoid", "usuarioid", "usuario", "alvo", "hashtags", "latitude", "longitude", "created_at", "updated_at")
