from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^shelters/$', 'abrigo.views.shelters'),
    url(r'^shelterDetail/(?P<place_id>[^\.]+)/$', 'abrigo.views.shelterDetail'),
    url(r'^sheltersList/(?P<country_short_name>[^\.]+)/$', 'abrigo.views.shelterList'),
    url(r'^admin/', include(admin.site.urls)),
)
