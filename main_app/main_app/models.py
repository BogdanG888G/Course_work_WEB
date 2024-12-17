from django.db import models
from django.db.models import JSONField
from django.contrib.postgres.fields import ArrayField

class Stand(models.Model):
    POWER_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    SPEED_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    RANGE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    DURABILITY_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    PRECISION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    POTENTIAL_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    stand_user = models.CharField(max_length=60, blank=True, null=True, db_index=True)
    stand_name = models.CharField(max_length=30, db_index=True)
    power = models.CharField(max_length=1, choices=POWER_CHOICES, blank=True, null=True)
    speed = models.CharField(max_length=1, choices=SPEED_CHOICES, blank=True, null=True)
    range = models.CharField(max_length=1, choices=RANGE_CHOICES, blank=True, null=True)
    durability = models.CharField(max_length=1, choices=DURABILITY_CHOICES, blank=True, null=True)
    precision = models.CharField(max_length=1, choices=PRECISION_CHOICES, blank=True, null=True)
    potential = models.CharField(max_length=1, choices=POTENTIAL_CHOICES, blank=True, null=True)
    stand_image = models.ImageField(upload_to='stand_images/', blank=True, null=True)
    user_image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    additional_info = models.JSONField(blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=50), blank=True, null=True,
                      default=list)


def __str__(self):
        return f"{self.stand_name} - {self.stand_user}"
