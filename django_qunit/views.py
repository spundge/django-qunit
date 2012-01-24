from django.conf import settings
from django.shortcuts import render
from django.utils import simplejson

import os

def load_configuration(path):
    try:
        file = open(os.path.join(path, 'suite.json'), 'r')
        json = file.read()
        return simplejson.loads(json)
    except:
        return {}


def get_suite_context(path):
    full_path = os.path.join(settings.QUNIT_TEST_DIRECTORY, path)
    path_iterator = os.walk(full_path)
    full_path, directories, files = path_iterator.next()

    subsuites = [os.path.relpath(walk[0], settings.QUNIT_TEST_DIRECTORY) for walk in path_iterator]



    suite = {}

    # set suite name
    pieces = path.split('/')
    if len(pieces) < 2:
        suite['name'] = 'main'
    else:
        suite['name'] = ''.join(pieces[-2])

    # defaults
    suite['qunit_js_files'] = []
    suite['qunit_css_files'] = []
    suite['absolute_urls'] = []
    suite['js_files'] = []

    # Load base suite configuration
    suite.update(load_configuration(settings.QUNIT_TEST_DIRECTORY))

    # load suite configuration
    suite.update(load_configuration(full_path))

    # Load necessary js and css from qunit directory, before any other specified.
    use_composite = False
    if subsuites and getattr(settings, 'QUNIT_USE_COMPOSITE', False):
        suite['qunit_js_files'].insert(0, 'qunit-composite.js')
        suite['qunit_css_files'].insert(0, 'qunit-composite.css')
        use_composite = True

    suite['qunit_js_files'].insert(0, 'qunit.js')
    suite['qunit_css_files'].insert(0, 'qunit.css')

    previous_directory = parent_directory(path)

    return {
        'files': [os.path.join(path, file) for file in files if file.endswith('js')],
        'previous_directory': previous_directory,
        'qunit_url': settings.QUNIT_URL,
        'js_url' : settings.QUNIT_JS_URL,
        'subsuites': subsuites,
        'suite': suite,
        'use_cmposite' : use_composite,
    }


def run_tests(request, path, template_name='qunit/index.html'):
    suite_context = get_suite_context(path)
    response =  render(request, template_name, suite_context)

    # When used by qunit-composite, test pages are rendered in iFrames
    # If the using site is using the X-Frame-Options header set to 'DENY',
    # this will cause the inclusion to fail. Setting the option to 'SAMEORIGIN'
    # will make the included iFrame accessible and is usually respected by middlewares
    # like django-secure.
    response['X-Frame-Options'] = 'SAMEORIGIN'
    return response


def parent_directory(path):
    """
    Get parent directory. If root, return None
    "" => None
    "foo/" => "/"
    "foo/bar/" => "foo/"
    """
    if path == '':
        return None
    prefix = '/'.join(path.split('/')[:-2])
    if prefix != '':
        prefix += '/'
    return prefix
