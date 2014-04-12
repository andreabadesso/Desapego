from django.shortcuts import render
from Usuarios.models import Usuario
from django.http import HttpResponse
from Usuarios.serializers import UsuarioSerializer
from rest_framework.renderers import JSONRenderer


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def verUsuario(request, fbid):
    try:
        usuario = Usuario.objects.get(fbId=fbid)
    except Usuario.DoesNotExist:
        usuario = Usuario(fbId=fbid)
        usuario.baixarInformacoes()

    serializer = UsuarioSerializer(usuario, many=False)
    return JSONResponse(serializer.data)


def usuario(request):
    fbid = request.GET.get("fbid")
    try:
        usuario = Usuario.objects.get(fbId=fbid)
    except Usuario.DoesNotExist:
        return HttpResponse("0")
    serializer = UsuarioSerializer(usuario, many=False)
    return JSONResponse(serializer.data)
