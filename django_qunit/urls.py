import os

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    url(r'^tests/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.QUNIT_TEST_DIRECTORY,
    }, name='qunit_test'),
    url('^(?P<path>.*)$', 'django_qunit.views.run_tests',
        name='qunit_test_overview'),
)
