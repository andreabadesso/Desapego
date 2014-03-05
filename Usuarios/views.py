from django.shortcuts import render
from Usuarios.models import Usuario
from django.shortcuts import render
from django.http import HttpResponse
from Usuarios.serializers import UsuarioSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def verUsuario(request):
    fbid = request.GET.get("fbid")
    try:
        usuario = Usuario.objects.get(fbId=fbid)
    except Usuario.DoesNotExist:
        usuario = Usuario(fbId=fbid)
        usuario.baixarInformacoes()

    return render(request, "usuario.html", { "usuario": usuario })


def usuario(request):
    fbid = request.GET.get("fbid")
    try:
        usuario = Usuario.objects.get(fbId=fbid)
    except Usuario.DoesNotExist:
        return HttpResponse("0")
    serializer = UsuarioSerializer(usuario, many=False)
    return JSONResponse(serializer.data)


