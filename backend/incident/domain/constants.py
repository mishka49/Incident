from django.db.models import TextChoices


class IncidentStatusChoice(TextChoices):
    NEW = "new", "Новый"
    ACCEPTED = "accepted", "Принят в работу"
    COMPLETED = "completed", "Выполнена"
    CANCELLED = "cancelled", "Отменена"


class SourceTypeChoice(TextChoices):
    OPERATOR = "operator", "Оператор"
    MONITORING = "monitoring", "Мониторинг"
    PARTNER = "partner", "Партнер"