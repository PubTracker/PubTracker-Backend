from django.http import HttpResponse
from django.core import serializers
import rsshandler
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def rss(request):
    result = rsshandler.rss_parse('http://jvi.asm.org/rss/current.xml')
    return HttpResponse(json.dumps(result), content_type='application/json')


