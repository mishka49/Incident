from django.db import models

from incident.domain.constants import IncidentStatusChoice, SourceTypeChoice


class Incident(models.Model):
    description = models.TextField(max_length=500, verbose_name="Описание")
    status = models.CharField(
        max_length=100,
        choices=IncidentStatusChoice.choices,
        default=IncidentStatusChoice.NEW,
    )
    source = models.CharField(
        max_length=100,
        choices=SourceTypeChoice.choices,
        default=SourceTypeChoice.MONITORING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Инцидент"
        verbose_name_plural = "Инциденты"
        ordering = ("-pk",)

    def __str__(self):
        return str(self.pk)



