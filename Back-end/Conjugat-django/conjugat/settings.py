"""
Django settings for conjugat project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from decouple import config, AutoConfig

# Choose the path where the env file is kept
config = AutoConfig(search_path='..\..\..\..\envs\Project 1 - Conjugat\.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['.ngrok.io',
    'localhost',
    '127.0.0.1',
    'conjugat.io',
    ]

CSRF_TRUSTED_ORIGINS = [
    'https://*.ngrok.io',
    'http://localhost',
    'http://127.0.0.1:8000',
    'http://conjugat.io',
    'https://conjugat.io',
    'http://localhost:5000',
    'http://localhost:4173'
]

# Application definition

INSTALLED_APPS = [
    'daphne',
    'channels',
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'subscription.apps.SubscriptionConfig',
    'verbs.apps.VerbsConfig',
    'settings.apps.SettingsConfig',
    'social_django',
    'newsletter.apps.NewsletterConfig',
    'django_extensions',
    'corsheaders',
    'rest_social_auth',
    'knox',
    'adjectives.apps.AdjectivesConfig',
    'nouns.apps.NounsConfig',
    'testFunctionality.apps.TestfunctionalityConfig',
    'django_cassandra_engine',
    'django_crontab',
    'social.apps.SocialConfig',
    'messagesFunctionality.apps.MessagesfunctionalityConfig',
    'battle.apps.BattleConfig',
    'tournament.apps.TournamentConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'conjugat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'settings.context_processors.theme',
            ],
        },
    },
]

ASGI_APPLICATION = 'conjugat.asgi.application'
WSGI_APPLICATION = 'conjugat.wsgi.application'

CHANNEL_LAYERS = {
    'default':{
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [("127.0.0.1", 6379)],
        }
    }
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB1_NAME'),
        'USER': config('DB1_USER'),
        'PASSWORD': config('DB1_PASSWORD')
    },
    'cassandra': {
         'ENGINE': 'django_cassandra_engine',
         'NAME': config('DB2_NAME'),
         'HOST': '127.0.0.1',
         'OPTIONS': {
             'replication': {
                 'strategy_class': 'SimpleStrategy',
                 'replication_factor': 1
             },
         }
     }
}
CASSANDRA_FALLBACK_ORDER_BY_PYTHON = True

# from gqlalchemy import Memgraph
# memgraph = Memgraph(host='127.0.0.1', port=7687)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config('CACHE_LOCATION'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD":config('CACHE_PASSWORD')
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
]


ENCRYPTION_KEY = str(config('ENCRYPTION_KEY')+'=').encode()

STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')
STRIPE_WEBHOOK_SECRET = config('STRIPE_WEBHOOK_SECRET')

PAYPAL_CLIENT_ID = config('PAYPAL_CLIENT_ID')
PAYPAL_SECRET_KEY = config('PAYPAL_SECRET_KEY')

COINBASE_COMMERCE_API_KEY = config('COINBASE_COMMERCE_API_KEY')
COINBASE_COMMERCE_WEBHOOK_SECRET = config('COINBASE_COMMERCE_WEBHOOK_SECRET')


# https://developers.facebook.com/apps/1081409575860175/settings/basic/
SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')

# https://console.cloud.google.com/apis/credentials?authuser=1&project=conjugat-372211
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# https://developer.twitter.com/en/portal/projects/1593184068740554752/apps/26377281/auth-settings
SOCIAL_AUTH_TWITTER_KEY = config('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = config('SOCIAL_AUTH_TWITTER_SECRET')


MAILCHIMP_API_KEY = config('MAILCHIMP_API_KEY')
MAILCHIMP_USERNAME = config('MAILCHIMP_USERNAME')
MAILCHIMP_REGION = config('MAILCHIMP_REGION')
MAILCHIMP_MARKETING_AUDIENCE_ID = config('MAILCHIMP_MARKETING_AUDIENCE_ID')

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5000",
    "http://www.localhost:5000",
    "http://localhost:4173"
]

# CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOW_HEADERS = [
#     "withCredentials",
#     "x-csrftoken",
#     "xsrfCookieName",
#     "xsrfHeaderName",
#     "authorization",
#     "content-type",
# ]

# CSRF_COOKIE_DOMAIN = [
#     "http://localhost:5000",
# ]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
    ],
}

REST_SOCIAL_OAUTH_ABSOLUTE_REDIRECT_URI = 'http://localhost:5000/account/oauth'

CRONJOBS = [
    ('* * 1 * *', 'django.core.management.call_command', ['cache-date-check']),
    ('* * 1 * *', 'django.core.management.call_command', ['unactivated-user-check']),
    ('* * 1 * *', 'django.core.management.call_command', ['subscription-removal-check']),
]
