from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['message', 'level', 'patient_name', 'created_at', 'is_resolved']
