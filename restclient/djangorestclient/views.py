import requests

from django.shortcuts 				import render
from django.views.generic 			import ListView

from .forms 						import DjangoRestClientForm

class DjangoRestClient(ListView):

	template_name = 'restclient.html'

	def get(self,request,*args,**kwargs):

		formObj					= DjangoRestClientForm(request.GET)
		response				= None
		error					= None
		msg 					= None
		if formObj.is_valid():

			formCleaned 		= formObj.cleaned_data
			url 				= formCleaned.get('url',None)
			method				= formCleaned.get('method','GET')
			headers				= formCleaned.get('headers','')
			body				= formCleaned.get('body','')

			print url

			if url is not None:

				if method	== 'GET':
					try:
						response 		= requests.get(url=url,params=body,headers=headers)
					except requests.exceptions.RequestException as e:
						error			= True
						msg				= e

				if method	== 'POST':

					try:
						response		= requests.post(url=url,params=body,headers=headers)
					except requests.exceptions.RequestExceptiona as e:
						error			= True
						msg				= e

		if not response and not error:
			error				= True
			msg					= "Unknown Exception occured"

		return render(request,self.template_name,{
				'form'		: formObj,
				'response'	: response,
				'error'		: error,
				'msg'		: msg
			})