from decouple import config
from pathlib import Path
from django.utils.translation import ugettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
	'modeltranslation',
	'registration',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'rest_framework',
	'ckeditor_uploader',
	'ckeditor',

	'foods',
	'order',
	'post',
	'pages',
	'users',
	'bot_users',
]
DEBUG = True
MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoProject3.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates']
		,
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

WSGI_APPLICATION = 'DjangoProject3.wsgi.application'

# DATABASES = {
#
# 	'default': {
#
# 		'ENGINE': 'django.db.backends.postgresql_psycopg2',
#
# 		'NAME': config('DB_NAME'),
#
# 		'USER': config('DB_USER'),
#
# 		'PASSWORD': config('DB_PASS'),
#
# 		'HOST': config('DB_HOST'),
#
# 		'PORT': config('DB_PORT'),
#
# 	}
#
# }
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
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]

LANGUAGE_CODE = 'en'

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LANGUAGES = (
	('en', _('English')),
	('uz', _('Uzbek')),
	('ru', _('Русский')),
)

LOCALE_PATHS = BASE_DIR / 'locale',

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = BASE_DIR / 'assets',

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
	'default': {
		'toolbar': 'full'
	},
}

ACCOUNT_ACTIVATION_DAYS = 3

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# EMAIL_HOST_USER = config('EMAIL_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_PASS')
EMAIL_HOST_USER = 'hellopython265@gmail.com'
EMAIL_HOST_PASSWORD = 'python#dev001'

# REST_FRAMEWORK = {
# 	'DEFAULT_PERMISSION_CLASSES': [
# 		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
# 	]
# }
try:
	from settings_locale import *
except ImportError:
	pass
