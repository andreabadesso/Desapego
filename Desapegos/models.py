from django.db import models
from Hashtags.models import Hashtag
from Status.models import Status
from Usuarios.models import Usuario
from Comentarios.models import Comentario
from django.core import serializers

class Desapego(models.Model):
	#usuarioFbId = models.CharField(max_length=150)
	usuario = models.ForeignKey(Usuario, related_name="desapegos")
	alvo = models.ForeignKey(Usuario, related_name="desapegados")
	hashtags = models.ManyToManyField(Hashtag, null=True, blank=True)
	status = models.ForeignKey(Status, null=True, blank=True)
	latitude = models.CharField(max_length=150, default="-", null=True)
	longitude = models.CharField(max_length=150, default="-", null=True)
	comentarios = models.ManyToManyField(Comentario, null=True, related_name="desapego")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def pegarAlvoId(self):
		return self.alvo.fbId

	alvoid	= property(pegarAlvoId)

	def pegarUsuarioId(self):
		return self.usuario.fbId

	usuarioid = property(pegarUsuarioId)

	def __unicode__(self):
		return "" + self.usuario.nome + " desapegou de " + self.alvo.nome

	def emJSON(self):
		data = serializers.serialize('json', [ self, ])
		return data

	class Meta:
		ordering = ('created_at',)
