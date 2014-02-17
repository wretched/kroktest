from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'krok.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^random/', 'kroktest.views.rnd'),
    url(r'^results/', 'kroktest.views.results'),
    url(r'^checked/', 'kroktest.views.checked'),
    url(r'^$', 'kroktest.views.home'),
)
