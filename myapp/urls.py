# encoding=utf8

from django.conf.urls import patterns, url, include

import views

urlpatterns = patterns("",
                       url("^$", views.index, name="index"),
                       )
