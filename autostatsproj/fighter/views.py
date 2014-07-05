from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic
from fighter.models import Fighter
import skripper

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'fighter/index.html'
	context_object_name = 'all_fighters'

	def get_queryset(self):
		return Fighter.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
	model = Fighter
	context_object_name = 'fighter'
	template_name = 'fighter/fighter.html'

	def get_object(self, *args, **kwargs):
		return get_object_or_404(Fighter, pk=self.kwargs['fighter_id'])

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		fighter = Fighter.objects.get(pk=self.kwargs['fighter_id'])
		if fighter.fight_status == 'W':
			fight_status = 'Won'
		elif fighter.fight_status == 'L':
			fight_status = 'Lost'
		elif fighter.fight_status == 'D':
			fight_status = 'Draw'		
		context['fight_status'] = fight_status
		return context