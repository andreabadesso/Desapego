from django.db import models
from Usuarios.models import Usuario


class Hashtag(models.Model):
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome


class Sugestao(models.Model):
    nome = models.CharField(max_length=150)
    usuario = models.ForeignKey(Usuario, null=True, blank=True)
    fbId = models.CharField(max_length=150)


class SugestaoUsuario(models.Model):
    texto = models.TextField()
    usuario = models.ForeignKey(Usuario, null=True, blank=True)
    fbId = models.CharField(max_length=150)
