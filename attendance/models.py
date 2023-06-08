from django.db import models
import uuid
from students.models import Student


class CheckInEvent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    time = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-time"]
