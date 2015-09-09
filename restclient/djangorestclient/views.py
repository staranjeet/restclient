from django.shortcuts import render

from django.views.generic import ListView

class DjangoRestClient(ListView):

	template_name = 'restclient.html'

	def get(self,request,*args,**kwargs):
		return render(request,self.template_name,{})