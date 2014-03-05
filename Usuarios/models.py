from django.db import models
from urllib2 import urlopen
from simplejson import loads
from django.core import serializers
from Amigos.models import Amigo

class Usuario(models.Model):
	fbId = models.CharField(max_length=150)
	link = models.URLField(blank=True, null=True)
	username = models.CharField(max_length=150, blank=True, null=True)
	nome = models.CharField(max_length=150, blank=True, null=True)
	sobrenome = models.CharField(max_length=150, blank=True, null=True)
	nome_completo = models.CharField(max_length=150, blank=True, null=True)
	sexo = models.CharField(max_length=150, blank=True, null=True)
	amigos = models.ManyToManyField("Usuario", blank=True, null=True)
	cadastrado = models.BooleanField(default=False)

	def __unicode__(self):
		if self.cadastrado:
			return self.nome_completo
		else:
			return self.fbId

	def baixarInformacoes(self):
		informacoes = loads(urlopen('http://graph.facebook.com/' + self.fbId).read())

		try: 
			self.link = informacoes["link"]
		except:
			self.link = "" 

		self.username = informacoes["username"]
		self.nome_completo = informacoes["name"]
		self.nome = informacoes["first_name"]
		self.sobrenome = informacoes["last_name"]
		self.sexo = "Masculino" if (informacoes["gender"] == "male") else "Feminino"
		self.cadastrado = True
		self.save()

	def emJSON(self):
		data = serializers.serialize('json', [ self, ])
		return data

	
