from django.conf import settings
from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_control
from django.views.static import serve

no_cache_serve = cache_control(max_age=0, no_cache=True, no_store=True)(serve)

urlpatterns = patterns('',
    url(r'^tests/(?P<path>.*)$', no_cache_serve, {
        'document_root': settings.QUNIT_TEST_DIRECTORY,
    }, name='qunit_test'),

    url('^(?P<path>.*)$', 'django_qunit.views.run_tests',
        name='qunit_test_overview'),
)
