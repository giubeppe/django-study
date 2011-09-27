from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kitchensink.views.home', name='home'),
    # url(r'^kitchensink/', include('kitchensink.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^statics/', 'statics.views.index'),
    url(r'^pagination/', 'pagination.views.list'),
    url(r'^composite/instruments', 'compositedata.views.instruments'),
    url(r'^composite/', 'compositedata.views.show'),
    url(r'^homepage/', 'homepage.views.index'),
)
