from django.shortcuts import render
from django.http import HttpResponse
from Desapegos.models import Desapego

def index(request):
	return render(request, "site.html")

def desapego(request, id):
	try:
		desapego = Desapego.objects.get(pk=id)
	except Desapego.DoesNotExist:
		return HttpResponse("Nao existe")

	return render(request, "desapego.html", {"desapego": desapego, "desapegador": desapego.usuario, "desapegado": desapego.alvo})
