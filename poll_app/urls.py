from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poll_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^polls/', include('poll.urls')),
    url(r'^$', include('poll.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
