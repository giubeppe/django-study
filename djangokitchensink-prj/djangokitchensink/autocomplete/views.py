# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.db.models import Q

from djangokitchensink.autocomplete.models import NameUrl

def index(request):
    return render_to_response("example.html")

def secondindex(request):
    return render_to_response("second-example.html")

def getfromquery(request):
    try:
        query = request.GET["query"]
        callback = request.GET["callback"]
        nameurls = NameUrl.objects.filter(Q(name__startswith=query.lower()))
        return render_to_response("query.html", {"callback": callback, "nameurls": nameurls})
    except:
        return HttpResponse("")

def runquery(request):
    query = request.GET["query"]
    
    try:
        nameurls = NameUrl.objects.filter(Q(name__startswith=query.lower()))
        return render_to_response("old_query.html", {"query": query, "nameurls": nameurls}) 
    except:
        return HttpResponse("")
    
        
def populate(request):
    NameUrl().populate()
    return HttpResponse("populated")
