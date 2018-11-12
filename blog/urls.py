
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index),
    path(r'toto', views.toto),
]
