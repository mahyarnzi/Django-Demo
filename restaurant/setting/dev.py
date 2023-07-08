from restaurant.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e-k0!+bc73ts&h%g654#5i%e_hs%&)bd-o7k%b_j4w4+(5he0c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics'
]

SITE_ID = 1

# SMTP Configuration
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_mail")

# Maintenance Mode
MAINTENANCE_MODE = int(os.environ.get("MAINTENANCE_MODE", 0))
SET_ENDTIME = '2023/08/08 16:00:00'