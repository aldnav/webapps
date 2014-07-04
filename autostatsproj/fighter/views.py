from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from fighter.models import Fighter

# Create your views here.
def index(request):
	all_fighters = Fighter.objects.order_by('-pub_date')
	context = RequestContext(request, {
		'all_fighters': all_fighters,
	})
	return render(request, 'fighter/index.html', context)

def detail(request, fighter_id):
	fighter = get_object_or_404(Fighter, pk=fighter_id)
	return render(request, 'fighter/detail.html', {'fighter':fighter})