# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    settings.QUNIT_TEST_DIRECTORY
except AttributeError:
    raise ImproperlyConfigured('Missing required setting QUNIT_TEST_DIRECTORY.')
