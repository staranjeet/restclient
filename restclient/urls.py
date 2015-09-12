from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static        import static
from django.conf	import settings

from djangorestclient.views import DjangoRestClient

urlpatterns = [
    # Examples:
    # url(r'^$', 'restclient.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',DjangoRestClient.as_view(),name="django-rest-client-view"),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
