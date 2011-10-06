from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView
from django.contrib import admin
from models import Frat

urlpatterns = patterns('',
	(r'^', 'frats.views.index'),
	(r'^(?P<frat_name>\w+)/$', 'frats.views.detail'),
	(r'^(?P<frat_name>\w+)/(?P<user_name>\w+)/$', 'frats.views.profile'),
)
