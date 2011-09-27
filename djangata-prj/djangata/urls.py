from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangata.views.home', name='home'),
    # url(r'^djangata/', include('djangata.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^sankme/', 'thesink.views.helloworld'),
    url(r'^search/', 'thesink.views.search'),
    url(r'^redirect/', 'thesink.views.redirectview'),
)
