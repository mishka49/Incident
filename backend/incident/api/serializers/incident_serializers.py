from rest_framework import serializers

from incident.domain.constants import IncidentStatusChoice
from incident.domain.models import Incident
from incident.domain.services import update_incident_status


class IncidentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Incident
        fields = (
            "id",
            "description",
            "status",
            "source",
            "created_at",
        )


class IncidentStatusUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=IncidentStatusChoice.choices)

    def update(self, instance, validated_data):
        new_status = validated_data.get("status", instance.status)
        return update_incident_status(instance, new_status)
