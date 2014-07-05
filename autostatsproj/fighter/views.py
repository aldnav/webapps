from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.views import generic
from fighter.models import Fighter
from fighter.forms import FighterForm
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
		if fighter.fight_status:
			if fighter.fight_status == 'W':
				fight_status = 'Won'
			elif fighter.fight_status == 'L':
				fight_status = 'Lost'
			elif fighter.fight_status == 'D':
				fight_status = 'Draw'		
			context['fight_status'] = fight_status
		return context

# def scrape(request):
# 	if request.POST:
# 		form = FighterForm(request.POST)
# 		if form.is_valid():
# 			form.save()

# 			return HttpResponseRedirect('fighter/index.html')
# 	else:
# 		form = FighterForm()

# 	args = {}
# 	args.update(csrf(request))
# 	args['form'] = form
# 	return render_to_response('fighter/index.html', args)

def scrape(request):
	if request.POST:
		fm_url = request.POST['fm_url']
		mma_url = request.POST['mma_url']
		if fm_url and mma_url:
			# scraper = skripper.Scraper(fm_url, mma_url)
			# scraper.start()
			# scraper.join()
			# data = scraper.data
			data = skripper.scrape_details(fm_url, mma_url)
			if data:
				try:
					fighter = Fighter.objects.get(name=data['name'])
				except Fighter.DoesNotExist:				
					fighter = Fighter(**data)
					fighter.save()
				print data
	# return HttpResponseRedirect('../')
	args = {}
	args.update(csrf(request))
	# args['form'] = form
	# return render_to_response('fighter/index.html', args)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'),'/')