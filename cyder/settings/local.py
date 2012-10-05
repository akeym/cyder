#filename is settings_local.py
import sys
import os

from .base import *


_base = os.path.dirname(__file__)
site_root = os.path.realpath(os.path.join(_base, '../'))
sys.path.append(site_root)
sys.path.append(site_root + '/adapters')
sys.path.append(site_root + '/libs')
sys.path.append(site_root + '/modules')
sys.path.append(site_root + '/vendor')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inventory_mozilla',
        'USER': 'root',
        'PASSWORD': 'B0G3Y',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET storage_engine=InnoDB',
            'charset' : 'utf8',
            'use_unicode' : True,
        },
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_general_ci',
    },
    # 'slave': {
    #     ...
    # },
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

REMOTE_LOGINS_ON = True

SYSADMINS = (
                'you@domain.com',
            )

BUILD_TEAM = (
                'you@domain.com',
              )

SERVICES_URL = SITE_URL = STATIC_URL = 'http://localhost:8000/'

WIKI_USER = ''
WIKI_PASSWORD = ''

USE_LDAP = False
if USE_LDAP:
    LDAP_HOST = 'localhost'
    LDAP_USER = ''
    LDAP_PASS = ''
BUG_URL = ''
#import mysite.monitor
#mysite.monitor.start(interval=1.0)
# Specify your custom test runner to use
#TEST_RUNNER='test_runner_with_coverage'

 # List of modules to enable for code coverage
#COVERAGE_MODULES = ['api.views']
#TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'
USER_SYSTEM_ALLOWED_DELETE = ('')
from jinja2 import FileSystemLoader, Environment
TEMPLATE_DIRS = (
    os.path.join(_base, 'templates'),
    site_root + '/templates'
)
DEV = True

env = Environment(loader=FileSystemLoader(TEMPLATE_DIRS))
def jinja_url(view_name, *args, **kwargs):
    from django.core.urlresolvers import reverse, NoReverseMatch
    try:
        return reverse(view_name, args=args, kwargs=kwargs)
    except NoReverseMatch:
        try:
            project_name = SETTINGS_MODULE.split('.')[0]
            return reverse(project_name + '.' + view_name,
                           args=args, kwargs=kwargs)
        except NoReverseMatch:
            return ''

env.filters['url'] = jinja_url
import logging
error = dict(level=logging.ERROR)
info = dict(level=logging.INFO)
debug = dict(level=logging.DEBUG)

LOGGING = {
    'loggers': {
        'product_details': error,
        'nose.plugins.manager': error,
        'django.db.backends': error,
        'elasticsearch': info,
        'inventory': debug,
    },
}

#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
API_ACCESS = ('GET','POST','PUT','DELETE')
SCRIPT_URL = 'https://localhost.com'
DESKTOP_EMAIL_ADDRESS = 'desktop@example.com'
FROM_EMAIL_ADDRESS = 'inventory@example.com'
DHCP_CONFIG_OUTPUT_DIRECTORY = '/data/dhcpconfig-autodeploy'
UNAUTHORIZED_EMAIL_ADDRESS = ('manager@example.com')
PISTON_IGNORE_DUPE_MODELS = True

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    'HIDE_DJANGO_SQL': False,
    'TAG': 'div',
    'ENABLE_STACKTRACES' : True,
}