
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

app_name='blog'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^toto', views.toto, name='toto'),
    url('^posts/(?P<id>[0-9]+)', views.show, name='show'),
#	ca fonctionne si je met p a la place de posts
#   url('^p/(?P<id>[0-9]+)', views.show, name='show'),
]
