from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from incident.domain.models import Incident
from incident.api.serializers.incident_serializers import IncidentSerializer, IncidentStatusUpdateSerializer


@extend_schema(tags=["Incidents"])
class IncidentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status"]

    @action(detail=True, methods=["patch"], url_path="change-status")
    def change_status(self, request, pk=None):
        incident = get_object_or_404(self.queryset, pk=pk)
        serializer = IncidentStatusUpdateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        incident.status = serializer.validated_data["status"]
        incident.save()

        return Response(IncidentSerializer(incident).data, status=status.HTTP_200_OK)
