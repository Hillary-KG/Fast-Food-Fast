from django.shortcuts import render
from django.views.generic View,CreateView

# Create your views here.
class Index(View):
	"""docstring for Index"""
	template_name = 'index.html'
	def get(request,self,*args,**kwargs):
		context = {}
		return render(request,self.template_name,context)

		
		