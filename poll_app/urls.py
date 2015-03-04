from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from poll_app.forms import ContactForm1, ContactForm2, ContactForm3
from poll_app.views import ContactWizard


urlpatterns = patterns('',
    # Examples:
    # to make application index as the home page defined in views.
    # url(r'^$', 'poll_app.views.home', name='home'),
    # to make appliction index as main_page defined in views
    url(r'^$', 'poll_app.views.main_page', name='main_page'),

    url(r'^first_map', 'poll_app.views.first_map'),
    # url(r'^blog/', include('blog.urls')),

    # # Login / logout.
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    # # url(r'^accounts/profile/$', 'django.contrib.auth.views.profile'),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
    #     name='logout'),

    url(r'^polls/', include('poll.urls', namespace='poll')),
    # To make poll index page to ne index page of whole application
    # url(r'^$', include('poll.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # adding url for articles app
    url(r'^articles/', include('articles.urls', namespace='articles')),

    #user auth urls
    url(r'^accounts/login/$', 'poll_app.views.login'),
    url(r'^accounts/auth/$', 'poll_app.views.auth_view'),
    url(r'^accounts/logout/$', 'poll_app.views.logout'),
    url(r'^accounts/loggedin/$', 'poll_app.views.loggedin'),
    url(r'^accounts/invalid/$', 'poll_app.views.invalid_login'),
    # registeration urls
    url(r'^accounts/register/$', 'poll_app.views.register_user'),
    url(r'^accounts/register_success/$', 'poll_app.views.register_success'),
    url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
)
