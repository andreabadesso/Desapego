from celery import Celery
from Usuarios.models import Usuario
from celery.decorators import task

app = Celery(broker='amqp://')

@task(max_retries=3)
def salvar_amigos(amigos, usuario):
	print usuario
	print amigos
	for amigo in amigos:
		try:
			a = Usuario.objects.get(fbId=amigo)
		except Usuario.DoesNotExist:
			a = Usuario(fbId=amigo)
			a.baixarInformacoes()
		
		usuario.amigos.add(a)

	usuario.save()
