from django.db import models
import uuid
from django.urls import reverse


class Student(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    student_phone = models.PositiveIntegerField(null=True, blank=True)
    birthday = models.DateField()
    payment_id = models.CharField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("student_detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
