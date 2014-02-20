from django.shortcuts import render
from django.http import HttpResponse
from Desapegos.models import Desapego
from Usuarios.models import Usuario
from Hashtags.models import Hashtag
from Status.models import Status
from urllib2 import urlopen
from simplejson import loads
from django.views.decorators.csrf import csrf_exempt
from Desapegos.serializers import DesapegoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Amigos.models import Amigo
from Desapegos.tasks import salvar_amigos
import json

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def lista_hashtags(request):
    """
    Lista todas as hashtags ou cria uma nova hashtag.
    """
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()
        serializer = HashtagSerializer(hashtags, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HashtagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

def index(request):
	desapegos = Desapego.objects.all()
        serializer = DesapegoSerializer(desapegos, many=True)
        return JSONResponse(serializer.data)

def verDesapego(request):
	desapegoId = request.GET.get("id")

	try:
		desapego = Desapego.objects.get(pk=desapegoId)
	except Desapego.DoesNotExist:
		return render(request, "desapego_nao_existe.html")
	else:
                serializer = DesapegoSerializer(desapego, many=False)
                return JSONResponse(serializer.data)
		#return render(request, "desapego.html", {"desapego": desapego})

@csrf_exempt
def meusDesapegos(request):
        uid = request.GET.get('uid', None)

        if uid == None:
            return HttpResponse("Uid faltando")

        try:
            usuario = Usuario.objects.get(fbId=uid)
        except Usuario.DoesNotExist:
            usuario = Usuario(fbId=uid)
            usuario.baixarInformacoes()

        desapegos = Desapego.objects.filter(usuario=usuario)
        serializer = DesapegoSerializer(desapegos, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def guardar_amigos(request):
    uid = request.POST.get('uid', None)
    lista_amigos = json.loads(request.POST.get("lista_amigos"))

    try: 
        usuario = Usuario.objects.get(fbId=uid)
        if not usuario.cadastrado:
            usuario.baixarInformacoes()
    except Usuario.DoesNotExist:
        usuario = Usuario(fbId=uid)
        usuario.baixarInformacoes()
    salvar_amigos.delay(usuario, lista_amigos)
    
    return HttpResponse("0")
        
@csrf_exempt
def desapegos_amigos(request):
        uid = request.GET.get('uid')
        desapegos = []

        try:
            usuario = Usuario.objects.get(fbId=uid)
            print "Usuario existe, " + usuario.nome_completo
        except Usuario.DoesNotExist:
            print "Usuario nao existe"
        else:
            amigos = usuario.amigos.filter(cadastrado=True)
            for amigo in amigos:
                if amigo.desapegos.count() > 0:
                    for desapego in amigo.desapegos.all():
                        desapegos.append(desapego)


        serializer = DesapegoSerializer(desapegos, many=True)
        return JSONResponse(serializer.data)
            

@csrf_exempt
def desapegar(request):
	objDesapego = json.loads(request.POST.get("str"))
	desapegador = objDesapego["usuario"]
	alvoId = objDesapego["alvo"]

	try:
		usuario = Usuario.objects.get(fbId=desapegador)
	except Usuario.DoesNotExist:
		usuario = Usuario(fbId=desapegador)
		usuario.baixarInformacoes()
	
	try:
		alvo = Usuario.objects.get(fbId=alvoId)
	except Usuario.DoesNotExist:
		alvo = Usuario(fbId=alvoId)
		alvo.baixarInformacoes()

	hashtags = []

	desapego = Desapego(usuario=usuario, alvo=alvo, \
                latitude=objDesapego["latitude"], longitude=objDesapego["longitude"])
	desapego.save()

	for hashtag in objDesapego["hashtags"]:
		desapego.hashtags.add(Hashtag.objects.get(pk=hashtag))
	
	desapego.status = Status.objects.get(pk=1)

	desapego.save()

	return HttpResponse(desapego.pk)

