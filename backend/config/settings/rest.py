from config.settings.base import DEBUG, API_DOCS_ENABLE

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework.authentication.SessionAuthentication"],
}

if not DEBUG or not API_DOCS_ENABLE:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
        "rest_framework.renderers.JSONRenderer"
    ]
