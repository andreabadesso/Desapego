from django.db import models
from Usuarios.models import Usuario

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario)
	comentario = models.CharField(max_length=256)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
