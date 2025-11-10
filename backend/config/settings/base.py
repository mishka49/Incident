from datetime import timedelta
from os import getenv
from pathlib import Path
from sys import argv

from django.utils.translation import gettext_lazy as _

HTTP_OR_HTTPS = "http://" if getenv("TLS_MODE", "off") == "off" else "https://"
SITE_HOST = getenv("SITE_HOST")

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = getenv("SECRET_KEY")

TESTING = "test" in argv or any("pytest" in a for a in argv)
DEBUG = getenv("DEBUG", "True") == "True" and not TESTING
API_DOCS_ENABLE = getenv("API_DOCS_ENABLE", "False") == "True"

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [f"http://{SITE_HOST}", f"https://{SITE_HOST}"]

ASGI_APPLICATION = "config.asgi.application"

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")


    def show_toolbar_callback(_: None) -> bool:
        return DEBUG

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

USE_TZ = True
USE_L10N = True
USE_I18N = True
LANGUAGE_CODE = "ru"
TIME_ZONE = "Europe/Moscow"
LANGUAGES = (("ru", _("Russian")), ("en", _("English")))

STATIC_URL = "/s/"
STATIC_ROOT = Path(BASE_DIR) / "static"
