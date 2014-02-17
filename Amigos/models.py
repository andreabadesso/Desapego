from django.db import models

class Amigo(models.Model):
	uid = models.CharField(max_length=150)
	amigo_rel = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)
