from django.conf.urls 	import url

from .views 			import DjangoRestClient

urlpatterns = [

	url(r'^$',DjangoRestClient.as_view(),name="django-rest-client-view"),

]