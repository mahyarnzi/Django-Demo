from restaurant.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e-k0!+bc73ts&h%g654#5i%e_hs%&)bd-o7k%b_j4w4+(5he0c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['mahyarnazari.ir', 'www.mahyarnazari.ir']

# INSTALLED_APPS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

STATIC_ROOT = '/home/mahyarna/public_html/restaurant/static'
MEDIA_ROOT = '/home/mahyarna/public_html/restaurant/media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics'
]

SITE_ID = 1

# SMTP Configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'mail.mahyarnazari.ir'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ.get('email_username')
EMAIL_HOST_PASSWORD = os.environ.get('email_password')
DEFAULT_FROM_EMAIL = 'info@mahyarnazari.ir'

# Maintenance Mode
MAINTENANCE_MODE = int(os.environ.get("MAINTENANCE_MODE", 0))
SET_ENDTIME = '2023/08/08 16:00:00'

# Security
CSRF_COOKIE_SECURE = True  # to avoid transmitting the CSRF cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True  # to avoid transmitting the session cookie over HTTP accidentally.
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 15768000  # 6 months
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'DENY'
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Strict'

# Compress CSS and JS
COMPRESS_ENABLED = True
