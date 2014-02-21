from django.shortcuts import render
from Status.models import Status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Status.serializers import StatusSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def todos(request):
    if request.method == 'GET':
        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)
        return JSONResponse(serializer.data)
