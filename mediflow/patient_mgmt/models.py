from django.db import models

class Patient(models.Model):
    ZONE_CHOICES = [('red', 'Red'), ('yellow', 'Yellow'), ('green', 'Green')]
    STATUS_CHOICES = [('waiting', 'Waiting'), ('in_treatment', 'In Treatment'), ('discharged', 'Discharged')]

    name = models.CharField(max_length=100)
    zone = models.CharField(max_length=10, choices=ZONE_CHOICES, default='green')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    department = models.CharField(max_length=50, default='General')
    wait_time = models.IntegerField(default=0)
    admitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    queue_count = models.IntegerField(default=0)
    avg_wait_time = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="normal")

    def __str__(self):
        return self.name