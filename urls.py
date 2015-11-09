from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sos_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^get/$', 'abrigo.views.get'),
    url(r'^getlocation/(?P<place_id>[^\.]+)/$', 'abrigo.views.getlocation'),
    url(r'^admin/', include(admin.site.urls)),
)
