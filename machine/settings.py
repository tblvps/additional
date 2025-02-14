
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from decouple import config

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

BASE_DIR = Path(__file__).resolve().parent.parent

#SECRET_KEY = 'django-insecure-sezyox_us4xelux$#mfaf+_(@fl03)th28cu1j-!_wjf-a+!6r'

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

DEBUG = True

ALLOWED_HOSTS = ['*']

ADMINS = (
     ('admin', 'tblvps@gmail.com'),
)
MANAGERS = ADMINS

SITE_ID = 1

LOGIN_URL = '/admin/login/'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "shahinmondal42bd@gmail.com"
EMAIL_HOST_PASSWORD = "fsyy spny fwbh qmjy"
DEFAULT_FROM_EMAIL = "shahinmondal42bd@gmail.com"


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'oauth2_provider.backends.OAuth2Backend',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.humanize",
    'allauth.usersessions',
    'django.contrib.sites',
    'allauth.headless',
    'rest_framework',
    'allauth.mfa',
    'oauth2_provider',
    'env',
    'accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.paypal',
    'allauth.socialaccount.providers.apple',
]

SOCIALACCOUNT_PROVIDERS = {}

SOCIALACCOUNT_FORMS = {
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
    'signup': 'allauth.socialaccount.forms.SignupForm',
}

MFA_FORMS = {
    'authenticate': 'allauth.mfa.base.forms.AuthenticateForm',
    'reauthenticate': 'allauth.mfa.base.forms.AuthenticateForm',
    'activate_totp': 'allauth.mfa.totp.forms.ActivateTOTPForm',
    'deactivate_totp': 'allauth.mfa.totp.forms.DeactivateTOTPForm',
    'generate_recovery_codes': 'allauth.mfa.recovery_codes.forms.GenerateRecoveryCodesForm',
}

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'allauth.usersessions.middleware.UserSessionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]

ROOT_URLCONF = 'machine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'machine.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
         'OPTIONS': {
            'min_length': 9,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEBUG = os.getenv('DEBUG', 'False') == 'True'

SECRET_KEY = os.getenv('SECRET_KEY')
#DATABASE_URL = os.getenv('DATABASE_URL')
#LINODE_API_TOKEN = os.getenv('LINODE_API_TOKEN')

#AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
#AUTH0_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID")
#AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET")

GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static'),
       os.path.join(BASE_DIR, 'static/js'),
       os.path.join(BASE_DIR, 'static/src'),
       os.path.join(BASE_DIR, 'static/img'),

]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ACCOUNT_LOGIN_BY_CODE_ENABLED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_SIGNUP_REDIRECT_URL = "/"
ACCOUNT_LOGIN_REDIRECT_URL = "/"
MFA_PASSKEY_LOGIN_ENABLED = True
MFA_PASSKEY_SIGNUP_ENABLED = True
MFA_SUPPORTED_TYPES = ["totp", "webauthn", "recovery_codes"]
MFA_PASSKEY_LOGIN_ENABLED = True
MFA_WEBAUTHN_ALLOW_INSECURE_ORIGIN = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}
