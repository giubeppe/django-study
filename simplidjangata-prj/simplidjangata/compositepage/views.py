# Create your views here.

from django.shortcuts import render_to_response

def index(request):
    name = "name is the name"
    return render_to_response('compositepage/parentpage.html', {"name": name, "loop": 2})