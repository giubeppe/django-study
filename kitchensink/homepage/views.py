# Create your views here.

from django.http import HttpResponse
from django.shortcuts import *

def index(request):
	return render_to_response('page.html')
