from django.contrib import admin
from .models import Patient, Admission, Ward, Bed

# Register your models here.
admin.site.register(Patient)
admin.site.register(Admission)
admin.site.register(Ward)
admin.site.register(Bed)