# -*- coding: utf-8 -*-
from django.conf.urls import *

from .views import IndexView


urlpatterns = patterns(
    '',
    url(r'/$', IndexView(), name='index'),
)
