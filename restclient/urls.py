from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'restclient.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/', include('djangorestclient.urls')),

    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
