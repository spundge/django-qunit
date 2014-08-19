# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    '',
    url('^qunit/', include('django_qunit.urls'))
)
