from django.forms import widgets
from rest_framework import serializers
from Status.models import Status

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ("id", "status", "created_at", "updated_at")
