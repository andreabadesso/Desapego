from __future__ import absolute_import
from Usuarios.models import Usuario
from celery import shared_task

@shared_task
def salvar_amigos(usuario, lista_de_amigos):
	numero = 0
	for amigo in lista_de_amigos:
		try:
			a = Usuario.objects.get(fbId=amigo)
		except Usuario.DoesNotExist:
			a = Usuario(fbId=amigo)
			a.save()
			numero += 1

		usuario.amigos.add(a)
		usuario.save()
	return numero
