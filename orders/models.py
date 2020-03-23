from django.db import models
from django.utils import timezone


class ItemOrder(models.Model):
    phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)


