from django.shortcuts import render
from Usuarios.models import Usuario

def verUsuario(request):
    fbid = request.GET.get("fbid")
    try:
        usuario = Usuario.objects.get(fbId=fbid)
    except Usuario.DoesNotExist:
        usuario = Usuario(fbId=fbid)
        usuario.baixarInformacoes()

    return render(request, "usuario.html", { "usuario": usuario })

