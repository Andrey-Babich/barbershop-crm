from django.contrib import admin

from .models import (
    Master,
    Service,
    Appointment
)


admin.site.register(Master)
admin.site.register(Service)
admin.site.register(Appointment)