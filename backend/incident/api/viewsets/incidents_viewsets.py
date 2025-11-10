from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from incident.domain.models import Incident
from incident.api.serializers.incident_serializers import IncidentSerializer, IncidentStatusUpdateSerializer


@extend_schema(tags=["Incidents"])
class IncidentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    http_method_names = ["get", "post", "patch"]
    queryset = Incident.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]

    def get_serializer_class(self):
        match self.action:
            case "partial_update":
                return IncidentStatusUpdateSerializer
            case _:
                return IncidentSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
