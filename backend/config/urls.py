from django.conf import settings
from django.urls import include, path

from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/incidents/", include("incident.api.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("api/v1/__debug__/", include(debug_toolbar.urls)),)

if settings.API_DOCS_ENABLE:
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

    urlpatterns += (
        path(
            "api/v1/docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="docs",
        ),
        path("api/v1/schema", SpectacularAPIView.as_view(), name="schema"),
    )
