from __future__ import unicode_literals
from __future__ import absolute_import
import ast
import os.path
import dj_database_url
import dj_email_url
from urllib import quote_plus as urlquote
from django.contrib.messages import constants as messages
# import django_cache_url
from celery.schedules import crontab

DEBUG = True
PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../..'))

SITE_ID = 1

ROOT_URLCONF = 'honeybadger.urls'

WSGI_APPLICATION = 'honeybadger.wsgi.application'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
INTERNAL_IPS = os.environ.get('INTERNAL_IPS', '127.0.0.1').split()

TIME_ZONE =  'Asia/Kolkata'
LANGUAGE_CODE = 'en-us'
LOCALE_PATHS = [os.path.join(PROJECT_ROOT, 'locale')]
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# CACHES = {'default': django_cache_url.config()}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'assets/',
        'STATS_FILE': os.path.join(PROJECT_ROOT, 'webpack-bundle.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': [
            r'.+\.hot-update\.js',
            r'.+\.map']}}




# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder'
# ]

# context_processors = [
#     'django.contrib.auth.context_processors.auth',
#     'django.template.context_processors.debug',
#     'django.template.context_processors.i18n',
#     'django.template.context_processors.media',
#     'django.template.context_processors.static',
#     'django.template.context_processors.tz',
#     'django.contrib.messages.context_processors.messages',
#     'django.template.context_processors.request',
#     'saleor.core.context_processors.default_currency',
#     'saleor.cart.context_processors.cart_counter',
#     'saleor.cart.context_processors.wish_counter',
#     'saleor.core.context_processors.search_enabled',
#     'saleor.site.context_processors.settings',
#     'saleor.core.context_processors.webpage_schema',
#     'social_django.context_processors.backends',
#     'social_django.context_processors.login_redirect',
# ]

loaders = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # TODO: this one is slow, but for now need for mptt?
    'django.template.loaders.eggs.Loader']


# Make this unique, and don't share it with anybody.
SECRET_KEY = "mdk8ap10p!rz2(xh9$sa@%grmz*xo)ef*^3m%r99(b2*2qive)"


def load_middleware():
    import os
    
    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        # 'saleor.registration.backends.CustomAuthentication.CustomAuthentication',    
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'babeldjango.middleware.LocaleMiddleware',
        'saleor.core.middleware.DiscountMiddleware',
        'saleor.core.middleware.GoogleAnalytics',
        'saleor.core.middleware.CountryMiddleware',
        'saleor.core.middleware.CurrencyMiddleware',
        # 'saleor.api.AuthorizationMiddleware.AuthorizationMiddleware',
        'social_django.middleware.SocialAuthExceptionMiddleware',
        # 'whitenoise.middleware.WhiteNoiseMiddleware',
        'django_user_agents.middleware.UserAgentMiddleware',
        'simple_history.middleware.HistoryRequestMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    if not os.path.isfile('./ENV') and not os.path.isfile('./STAGE_ENV') :
        MIDDLEWARE_CLASSES.insert(0,'saleor.middleware.BaseMiddleware.BaseMiddleware')
    return MIDDLEWARE_CLASSES

""" loading the middleware """        
MIDDLEWARE_CLASSES = load_middleware()

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
    'OPTIONS': {
        'debug': DEBUG,
        'context_processors': context_processors,
        'loaders': loaders,
        'string_if_invalid': '<< MISSING VARIABLE "%s" >>' if DEBUG else ''}}]


DEFAULT_COUNTRY = 'IN'
DEFAULT_CURRENCY = 'INR'
AVAILABLE_CURRENCIES = [DEFAULT_CURRENCY]


LOGIN_REDIRECT_URL = 'home'

PAGINATE_BY = 16

BOOTSTRAP3 = {
    'set_placeholder': False,
    'set_required': False,
    'success_css_class': '',
    # 'form_renderers': {
    #     'default': 'saleor.core.utils.form_renderer.FormRenderer',
    # },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
    

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

LOGOUT_ON_PASSWORD_CHANGE = False

import djcelery
djcelery.setup_loader()
