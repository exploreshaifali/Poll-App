from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns('',
    # url(r'^$', views.article_index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^all/$', 'articles.views.article_all'),
    url(r'^get/(?P<article_id>\d+)/$', 'articles.views.article'),
)