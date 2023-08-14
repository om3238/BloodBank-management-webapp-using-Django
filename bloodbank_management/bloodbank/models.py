from django.db import models

class BloodBank(models.Model):
    blood_group_choices = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=3, choices=blood_group_choices)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"

