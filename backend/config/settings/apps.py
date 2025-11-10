from os import getenv

DEBUG = getenv("DEBUG", "True") == "True"

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.postgres",
    "django.forms",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "django_filters",
    "drf_spectacular",
    "rest_framework",
]

LOCAL_APPS = [
    "incident.apps.IncidentConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")


    def show_toolbar_callback(_: None) -> bool:
        return DEBUG


    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": "config.settings.show_toolbar_callback"
    }
