from django.db import models

class Bed(models.Model):
    STATUS_CHOICES = [('clean', 'Clean'), ('dirty', 'Dirty'), ('occupied', 'Occupied')]

    bed_number = models.CharField(max_length=10)
    ward = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='clean')

    def __str__(self):
        return f"Bed {self.bed_number}"
