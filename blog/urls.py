
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index),
    url('^toto', views.toto),
    url('^posts/(?P<id>[0-9]+)', views.show),
]
