from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns('',
    # url(r'^$', views.article_index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
)
