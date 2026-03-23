from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    queue_count = models.IntegerField(default=0)
    avg_wait_time = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="normal")

    def __str__(self):
        return self.name
