from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplidjangata.views.home', name='home'),
    # url(r'^simplidjangata/', include('simplidjangata.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'helloworld.views.helloworld'),
    url(r'^compositepage/', 'compositepage.views.index'),
    url(r'^email/', include('emails.urls'))
)
