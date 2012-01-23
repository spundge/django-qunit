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

    subsuites = [dirpath for dirpath, dirs, files in path_iterator]

    suite = {}

    # set suite name
    pieces = path.split('/')
    if len(pieces) < 2:
        suite['name'] = 'main'
    else:
        suite['name'] = ''.join(pieces[-2])

    # defaults
    suite['qunit_files'] = []
    suite['absolute_urls'] = []
    suite['static_urls'] = []

    # Load base suite configuration
    suite.update(load_configuration(settings.QUNIT_TEST_DIRECTORY))

    # load suite configuration
    suite.update(load_configuration(full_path))

    previous_directory = parent_directory(path)

    return {
        'files': [path + file for file in files if file.endswith('js')],
        'previous_directory': previous_directory,
        'qunit_url': settings.QUNIT_URL,
        'subsuites': subsuites,
        'suite': suite,
    }


def run_tests(request, path, template_name='qunit/index.html'):
    suite_context = get_suite_context(path)
    return render(request, template_name, suite_context)


def parent_directory(path):
    """
    Get parent directory. If root, return ""
    "" => ""
    "foo/" => "/"
    "foo/bar/" => "foo/"
    """
    parent = os.path.dirname(path)
    if parent and not parent.endswith('/'):
        parent += '/'
    return parent
