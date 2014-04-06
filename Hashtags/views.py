from Hashtags.models import Hashtag, Sugestao
from Usuarios.models import Usuario
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Hashtags.serializers import HashtagSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def sugerir_hashtag(request):
    if request.method == "POST":
        hashtag = request.POST.get("hashtag")
        usuario = request.POST.get("fbid")
        try:
            user = Usuario.objects.get(fbId=usuario)
        except Usuario.DoesNotExist:
            sugestao = Sugestao(nome=hashtag, fbId=usuario)
        else:
            sugestao = Sugestao(usuario=user, nome=hashtag, fbId=usuario)

        sugestao.save()
        return HttpResponse("0")
    else:
        return HttpResponse("-1")


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
