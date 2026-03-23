from django.db import models

class Alert(models.Model):
    LEVEL_CHOICES = [('critical', 'Critical'), ('warning', 'Warning'), ('info', 'Info')]
    message = models.TextField()
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='warning')
    patient_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.message
