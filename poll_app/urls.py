from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # to make application index as the home page defined in views.
    # url(r'^$', 'poll_app.views.home', name='home'),
    # to make appliction index as main_page defined in views
    url(r'^$', 'poll_app.views.main_page', name='main_page'),
    # url(r'^blog/', include('blog.urls')),

    # Login / logout.
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # url(r'^accounts/profile/$', 'django.contrib.auth.views.profile'),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    url(r'^polls/', include('poll.urls', namespace='poll')),
    # To make poll index page to ne index page of whole application
    # url(r'^$', include('poll.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
