from rest_framework.routers import DefaultRouter

from incident.api.viewsets.incidents_viewsets import IncidentViewSet

router = DefaultRouter()
router.register(r"", IncidentViewSet, basename="incident")

urlpatterns = router.urls
