from django.db import models

class Hashtag(models.Model):
	nome = models.CharField(max_length=150)
	sexo = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.nome
