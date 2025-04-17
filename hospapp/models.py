from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# app/models.py
class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    date_registered = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='patient_photos/', blank=False, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
