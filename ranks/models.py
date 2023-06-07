from django.db import models
import uuid
from students.models import Student


class Rank(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=50)
    alt_name = models.CharField(max_length=50, null=True, blank=True)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
