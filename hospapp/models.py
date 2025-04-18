from django.db import models
from django.utils import timezone

class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default='O+')
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='patient_photos/', blank=False, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Ward(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Bed(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='beds')
    bed_number = models.CharField(max_length=20)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ward.name} - {self.bed_number}"

class Admission(models.Model):
    STATUS_CHOICES = [
        ('Admitted', 'Admitted'),
        ('Discharged', 'Discharged'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField(default=timezone.now)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True)
    bed = models.ForeignKey(Bed, on_delete=models.SET_NULL, null=True)
    doctor_assigned = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Admitted')
    discharge_date = models.DateField(blank=True, null=True)
    discharge_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient} - {self.status}"
