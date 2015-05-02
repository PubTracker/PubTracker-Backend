from django.shortcuts import render
from django.http import HttpResponse
import rsshandler

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def rss(request):
    return rsshandler.rss_parse('')


