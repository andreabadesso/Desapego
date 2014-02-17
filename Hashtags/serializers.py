from django.forms import widgets
from rest_framework import serializers
from Hashtags.models import Hashtag

class HashtagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hashtag 
		fields = ("id", "nome", "sexo", "created_at", "updated_at")
