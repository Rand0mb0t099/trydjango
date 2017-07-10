#from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
# function based views
def home(request):
	html_var = 'a jiffy	<p>asdfasdf</p>'
	return render(request, "base.html", {"html_var":html_var} ) #response

class HomeView(TemplateView):
	template_name = 'base.html'
	def get_context_date(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

class ContactView(TemplateView):
	template_name = 'contact.html'
	def get_context_data(self, *args, **kwargs):
		context = super(ContactView, self).get_context_data(*args, **kwargs)
		print(context)
		return context