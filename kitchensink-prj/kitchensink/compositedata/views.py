# Create your views here.

from django.http import *
from django.shortcuts import *

from models import *

def show(request):
	albums = Album.objects.all()
	return render_to_response('album/show.html', {'albums': albums})

def instruments(request):
	instruments = { m.instrument for m in Musician.objects.all() }
	return render_to_response('album/instruments.html', {'instruments': instruments})

