from django.contrib import admin
from .models import CheckInEvent


# Register your models here.
class CheckInEventAdmin(admin.ModelAdmin):
    readonly_fields = ["time"]


admin.site.register(CheckInEvent, CheckInEventAdmin)
