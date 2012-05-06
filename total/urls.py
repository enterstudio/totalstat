from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'total.views.home', name='home'),
    # url(r'^total/', include('total.foo.urls')),
    url(r'^home$', 'book_statistics.views.home'),
    url(r'^work$', 'book_statistics.views.work'),
    url(r'^hello$', 'book_statistics.views.hello_world')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
