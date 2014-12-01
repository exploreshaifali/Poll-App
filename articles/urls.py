from django.conf.urls import patterns, url
from django.template.loader import get_template

from articles import views

urlpatterns = patterns('',
    url(r'^$', views.article_index, name='index'),
)
