from django.shortcuts import render
from django.http import HttpResponse
from urllib2 import urlopen
from simplejson import loads
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Comentarios.serializers import ComentarioSerializer
from Desapegos.models import Desapego
from Comentarios.models import Comentario
from Usuarios.models import Usuario

import json

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def todos_comentarios(request):
	try:
		desapego = Desapego.objects.get(pk=request.GET.get("id"))
	except Desapego.DoesNotExist:
		return HttpResponse("-1")

	data = Comentario.objects.filter(desapego=desapego)
        serializer = ComentarioSerializer(data, many=True)

        return JSONResponse(serializer.data)

@csrf_exempt
def comentar(request):
	try:
		desapego = Desapego.objects.get(pk=request.GET.get("id"))
	except Desapego.DoesNotExist:
		return HttpResponse("-1")


	try: 
		usuario = Usuario.objects.get(fbId=request.GET.get("fbid"))
	except Usuario.DoesNotExist:
		return HttpResponse("-1")

	c = request.GET.get("comentario")

	comentario = Comentario(usuario=usuario, comentario=c)
	comentario.save()

	desapego.comentarios.add(comentario)
	desapego.save()

	return HttpResponse(comentario.comentario)
