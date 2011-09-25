from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('autocomplete.views',
    url(r'^runquery', 'runquery'),
    url(r'^getfromquery', 'getfromquery'),
    url(r'^populate', 'populate'),
    url(r'^2nd', 'secondindex'),
    url(r'^', 'index'),
)
