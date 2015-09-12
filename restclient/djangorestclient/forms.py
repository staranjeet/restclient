from django import forms

class DjangoRestClientForm(forms.Form):

	url = forms.CharField(
		label		='Url',
		required 	= True,
		help_text	= 'Specify Url here',
		widget 		= forms.URLInput(attrs={'class':'form-control','placeholder':'Url'})
		)

	method = forms.ChoiceField(
		label		= 'Request method',
		required 	= True,
		help_text 	= 'Specify Url here',
		choices		= (('GET','GET'),('POST','POST')),
		widget		= forms.Select(attrs={'class':'form-control','placeholder':'Request method','style':'width:100%;'})
		)

	headers = forms.CharField(
		label		= 'Request headers here',
		required 	= False,
		help_text 	= 'Request headers here',
		widget 		= forms.Textarea(attrs={'class':'form-control','placeholder':'Enter header in the form of a=b&c=d','rows':5})
		)

	body = forms.CharField(
		label		= 'Request Body here',
		required	= False,
		help_text 	= 'Request Body here',
		widget		= forms.Textarea(attrs={'class':'form-control','placeholder':'Enter request body like a=b&c=d','rows':5})
		)