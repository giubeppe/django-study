# Create your views here.

from django.http import *
from django.shortcuts import *
from django.core.paginator import *

from models import Data

def list(request):
	all_data  = Data.objects.all()
	paginator = Paginator(all_data, 25)

	page = request.GET.get('page')
	try:
		page_data = paginator.page(page)
	except PageNotAnInteger:
		page_data = paginator.page(1)
	except EmptyPage:
		page_data = paginator.page(paginator.num_pages)

	return render_to_response('list.html', {'d': page_data})
	
