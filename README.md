django-qunit
============

django-qunit integrates the [QUnit Javascript testing framework][1] with
[Django][2], making it possible to run QUnit tests alongside your Django
app and test Ajax routines.

  [1]: http://docs.jquery.com/QUnit
  [2]: http://www.djangoproject.com/

installation
============

 1. Add 'django_qunit' to your settings.INSTALLED_APPS.
 2. Add settings.QUNIT_TEST_DIRECTORY, containing the path to your JavaScript test files.
 3. Add settings.QUNIT_URL, containing the root url of the QUnit JavaScript and CSS.
 4. Add settings.QUNIT_JS_URL, containing the root url of the JavaScript files that can be loaded by the suite configuration.
 5. Add settings.QUNIT_USE_COMPOSITE, to try to use the qunit-composite addon to run all subsuites from the top-level page.
 6. Add a urlconf to include('django_qunit.urls').
 7. Visit the URL you've included in your urlconf, and it should display QUnit test results.

*See the example in the tarball for more information.*

license
=======

Copyright (c) 2010 Cody Soyland
Licensed new-style BSD, also containing QUnit, which is licensed MIT. See LICENSE file for more information.
